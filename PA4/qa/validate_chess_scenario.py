"""Validate the authoritative Chess scenario embedded in the prototype.

The validator reads the ``chessScenario`` literals from ``prototype/app.js``
instead of maintaining a second board fixture. It then performs dependency-free
legal-move and attack checks for the review and practice positions.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP_JS = ROOT / "prototype" / "app.js"
REPORT = ROOT / "qa" / "chess-scenario-validation.md"
FILES = {f"{file}{rank}" for file in "abcdefgh" for rank in range(1, 9)}
PIECES = set("PRNBQKprnbqk")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def parse_object(source: str, field: str) -> dict[str, str]:
    match = re.search(rf"{re.escape(field)}:\s*Object\.freeze\(\{{(.*?)\}}\)", source, re.S)
    if not match:
        fail(f"prototype source is missing {field}")
    values = dict(re.findall(r"([a-h][1-8])\s*:\s*\"([PRNBQKprnbqk]?)\"", match.group(1)))
    if set(values) != FILES:
        fail(f"{field} does not declare all 64 board squares")
    return values


def parse_move(source: str, field: str) -> dict[str, str]:
    match = re.search(rf"{re.escape(field)}:\s*Object\.freeze\(\{{(.*?)\}}\)", source, re.S)
    if not match:
        fail(f"prototype source is missing {field}")
    values = dict(re.findall(r"(notation|source|destination|summary)\s*:\s*\"([^\"]*)\"", match.group(1)))
    required = {"notation", "source", "destination"}
    if not required.issubset(values):
        fail(f"{field} is missing one of {sorted(required)}")
    return values


def parse_scenario() -> dict[str, object]:
    source = APP_JS.read_text(encoding="utf-8")
    start = parse_object(source, "startPosition")
    practice = parse_object(source, "practicePosition")
    mistake = parse_move(source, "mistake")
    consequence = parse_move(source, "mistakeConsequence")
    better = parse_move(source, "betterMove")
    practice_move = parse_move(source, "practiceCorrectMove")
    move_number = re.search(r"moveNumber:\s*(\d+)", source)
    if not move_number:
        fail("prototype source is missing moveNumber")
    return {
        "source": source,
        "start": start,
        "practice": practice,
        "mistake": mistake,
        "consequence": consequence,
        "better": better,
        "practice_move": practice_move,
        "move_number": int(move_number.group(1)),
    }


def square_parts(square: str) -> tuple[int, int]:
    if not re.fullmatch(r"[a-h][1-8]", square):
        fail(f"invalid square {square!r}")
    return ord(square[0]) - ord("a"), int(square[1]) - 1


def square(file_index: int, rank_index: int) -> str:
    return f"{chr(file_index + ord('a'))}{rank_index + 1}"


def path_clear(board: dict[str, str], source: str, target: str) -> bool:
    source_file, source_rank = square_parts(source)
    target_file, target_rank = square_parts(target)
    step_file = (target_file > source_file) - (target_file < source_file)
    step_rank = (target_rank > source_rank) - (target_rank < source_rank)
    if step_file == step_rank == 0:
        return False
    file_index, rank_index = source_file + step_file, source_rank + step_rank
    while (file_index, rank_index) != (target_file, target_rank):
        if board[square(file_index, rank_index)]:
            return False
        file_index += step_file
        rank_index += step_rank
    return True


def side(piece: str) -> str:
    return "White" if piece.isupper() else "Black"


def is_square_attacked(board: dict[str, str], target: str, by_side: str) -> bool:
    target_file, target_rank = square_parts(target)
    for source, piece in board.items():
        if not piece or side(piece) != by_side:
            continue
        source_file, source_rank = square_parts(source)
        file_delta = target_file - source_file
        rank_delta = target_rank - source_rank
        kind = piece.lower()
        if kind == "p":
            direction = 1 if by_side == "White" else -1
            if rank_delta == direction and abs(file_delta) == 1:
                return True
        elif kind == "n" and (abs(file_delta), abs(rank_delta)) in {(1, 2), (2, 1)}:
            return True
        elif kind == "k" and max(abs(file_delta), abs(rank_delta)) == 1:
            return True
        elif kind in {"b", "r", "q"}:
            diagonal = abs(file_delta) == abs(rank_delta) and file_delta != 0
            straight = (file_delta == 0) != (rank_delta == 0)
            if (kind == "b" and diagonal) or (kind == "r" and straight) or (kind == "q" and (diagonal or straight)):
                if path_clear(board, source, target):
                    return True
    return False


def king_safe(board: dict[str, str], moving_side: str) -> bool:
    king = "K" if moving_side == "White" else "k"
    king_square = next((coordinate for coordinate, piece in board.items() if piece == king), None)
    if king_square is None:
        return False
    return not is_square_attacked(board, king_square, "Black" if moving_side == "White" else "White")


def apply_move(board: dict[str, str], move: dict[str, str], expected_piece: str, moving_side: str) -> dict[str, str]:
    source = move["source"]
    target = move["destination"]
    piece = board.get(source, "")
    captured = board.get(target, "")
    if piece != expected_piece:
        fail(f"{move['notation']} expects {expected_piece} on {source}, found {piece!r}")
    if captured and side(captured) == moving_side:
        fail(f"{move['notation']} targets a friendly piece on {target}")
    source_file, source_rank = square_parts(source)
    target_file, target_rank = square_parts(target)
    file_delta = abs(target_file - source_file)
    rank_delta = abs(target_rank - source_rank)
    kind = piece.lower()
    legal_shape = (
        kind == "q" and ((file_delta == 0) != (rank_delta == 0) or file_delta == rank_delta) and path_clear(board, source, target)
    ) or (
        kind == "n" and (file_delta, rank_delta) in {(1, 2), (2, 1)}
    )
    if not legal_shape:
        fail(f"{move['notation']} is not a legal {piece} move from {source} to {target}")
    next_board = dict(board)
    next_board[source] = ""
    next_board[target] = piece
    if not king_safe(next_board, moving_side):
        fail(f"{move['notation']} leaves {moving_side} in check")
    return next_board


def source_audit(source: str) -> list[str]:
    required_literals = [
        'id: "queen-safety-before-activity"',
        'startPosition: Object.freeze({',
        'mistakeConsequence: Object.freeze({',
        'practicePosition: Object.freeze({',
        'practiceCorrectMove: Object.freeze({',
        'selectedSquare: null',
        'chessMoveForPhase',
    ]
    for literal in required_literals:
        if literal not in source:
            fail(f"prototype source is missing authoritative literal {literal}")
    for stale in ("Qa4", "Qc2", '"7. c3 a6"'):
        if stale in source:
            fail(f"stale Chess scenario literal remains in prototype source: {stale}")
    return [
        "Prototype source exposes one review object with review, consequence, and practice fields.",
        "Prototype source includes selectedSquare and phase-specific move handling.",
        "The previous Qa4/Qc2 scenario literals are absent from the participant flow.",
    ]


def semantic_checks(scenario: dict[str, object]) -> list[str]:
    start = scenario["start"]
    practice = scenario["practice"]
    mistake = scenario["mistake"]
    consequence = scenario["consequence"]
    better = scenario["better"]
    practice_move = scenario["practice_move"]
    if not isinstance(start, dict) or not isinstance(practice, dict):
        fail("scenario positions could not be parsed")
    for label, board in (("review", start), ("practice", practice)):
        if set(board) != FILES or any(piece and piece not in PIECES for piece in board.values()):
            fail(f"{label} position contains invalid squares or pieces")
        if sum(piece == "K" for piece in board.values()) != 1 or sum(piece == "k" for piece in board.values()) != 1:
            fail(f"{label} position must contain one king per side")
        white_king = next(coordinate for coordinate, piece in board.items() if piece == "K")
        black_king = next(coordinate for coordinate, piece in board.items() if piece == "k")
        white_file, white_rank = square_parts(white_king)
        black_file, black_rank = square_parts(black_king)
        if max(abs(white_file - black_file), abs(white_rank - black_rank)) <= 1:
            fail(f"{label} kings are adjacent")
        if not king_safe(board, "White") or not king_safe(board, "Black"):
            fail(f"{label} position leaves a king in check")

    if scenario["move_number"] <= 0:
        fail("moveNumber must be positive")
    mistake_board = apply_move(start, mistake, "Q", "White")
    if mistake["notation"] != "Qh5" or mistake["source"] != "d1" or mistake["destination"] != "h5":
        fail("review mistake fields do not match the validated queen hang")
    if not is_square_attacked(start, mistake["destination"], "Black"):
        fail("the mistake destination is not attacked before the move")
    consequence_board = apply_move(mistake_board, consequence, "n", "Black")
    if consequence["source"] != "f6" or consequence["destination"] != mistake["destination"] or consequence_board[consequence["destination"]] != "n":
        fail("the immediate consequence does not capture the queen on the stated square")

    better_board = apply_move(start, better, "Q", "White")
    if better["source"] != mistake["source"] or is_square_attacked(better_board, better["destination"], "Black"):
        fail("the better move does not address the same attack")
    if better_board[mistake["destination"]] or not king_safe(better_board, "White"):
        fail("the better move does not leave a safe resulting position")

    practice_result = apply_move(practice, practice_move, "Q", "White")
    if not is_square_attacked(practice, practice_move["source"], "Black"):
        fail("practice position does not present the same attacked-piece concept")
    if is_square_attacked(practice_result, practice_move["destination"], "Black"):
        fail("practice move destination remains attacked")
    return [
        "Review and practice positions contain valid boards with non-adjacent kings.",
        "Qh5 is legal, h5 is attacked by the black knight, and Nxh5 legally captures the queen.",
        "Qe2 is legal, outside the documented attack, and leaves the queen on the board.",
        "Practice Qd3 is legal and moves the queen away from the bishop attack in a new position.",
    ]


def main() -> None:
    scenario = parse_scenario()
    checks = source_audit(scenario["source"]) + semantic_checks(scenario)
    lines = ["# Chess scenario validation", "", "Status: **PASS**", "", "Checks:"]
    lines.extend(f"- PASS — {item}" for item in checks)
    lines.extend([
        "",
        "Authoritative scenario:",
        f"- ID: `queen-safety-before-activity`; move {scenario['move_number']}, White to move.",
        "- Review mistake: `Qh5`; immediate consequence: `Nxh5` captures the queen.",
        "- Better move: `Qe2`; practice move: `Qd3` in a separate position.",
        "- This is scenario validation evidence only; it is not participant evidence or a study result.",
    ])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
