# Chess scenario validation

Status: **PASS**

Checks:
- PASS — Prototype source exposes one review object with review, consequence, and practice fields.
- PASS — Prototype source includes selectedSquare and phase-specific move handling.
- PASS — The previous Qa4/Qc2 scenario literals are absent from the participant flow.
- PASS — Review and practice positions contain valid boards with non-adjacent kings.
- PASS — Qh5 is legal, h5 is attacked by the black knight, and Nxh5 legally captures the queen.
- PASS — Qe2 is legal, outside the documented attack, and leaves the queen on the board.
- PASS — Practice Qd3 is legal and moves the queen away from the bishop attack in a new position.

Authoritative scenario:
- ID: `queen-safety-before-activity`; move 12, White to move.
- Review mistake: `Qh5`; immediate consequence: `Nxh5` captures the queen.
- Better move: `Qe2`; practice move: `Qd3` in a separate position.
- This is scenario validation evidence only; it is not participant evidence or a study result.
