from __future__ import annotations

import csv
import hashlib
import json
import os
import subprocess
from pathlib import Path

import pdfplumber
from PIL import Image


PA1 = Path(r"C:\Users\Administrator\Documents\MEGA\tkgd\PA1")
PA2 = Path(r"C:\Users\Administrator\Documents\MEGA\tkgd\PA2")
OUT = PA2 / "tmp" / "source-audit"
TEXT_OUT = OUT / "pdf-text"

TEXT_EXTENSIONS = {".txt", ".md", ".csv", ".json", ".yml", ".yaml"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".svg"}
SKIP_PARTS = {"node_modules", "__pycache__", ".git"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def relative_label(path: Path) -> str:
    for root in (PA1, PA2):
        try:
            return f"{root.name}/{path.relative_to(root).as_posix()}"
        except ValueError:
            pass
    return str(path)


def is_skipped(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def pdf_record(path: Path) -> dict:
    pages: list[dict] = []
    with pdfplumber.open(path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text(x_tolerance=2, y_tolerance=3) or ""
            pages.append(
                {
                    "page": page_number,
                    "width": round(float(page.width), 2),
                    "height": round(float(page.height), 2),
                    "text": text,
                }
            )
    safe_name = relative_label(path).replace("/", "__").replace("\\", "__")
    text_path = TEXT_OUT / f"{safe_name}.txt"
    text_path.write_text(
        "\n\n".join(
            f"===== PAGE {page['page']} =====\n{page['text']}" for page in pages
        ),
        encoding="utf-8",
    )
    return {
        "path": str(path),
        "relative": relative_label(path),
        "size": path.stat().st_size,
        "sha256": sha256(path),
        "pages": pages,
        "text_output": str(text_path),
    }


def image_record(path: Path) -> dict:
    record = {
        "path": str(path),
        "relative": relative_label(path),
        "size": path.stat().st_size,
        "sha256": sha256(path),
        "width": None,
        "height": None,
        "mode": None,
        "format": path.suffix.lower().lstrip("."),
    }
    if path.suffix.lower() != ".svg":
        try:
            with Image.open(path) as image:
                record.update(
                    width=image.width,
                    height=image.height,
                    mode=image.mode,
                    format=image.format,
                )
        except Exception as exc:
            record["image_error"] = str(exc)
    return record


def git_record(root: Path) -> dict:
    git = Path(
        r"C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime"
        r"\dependencies\native\git\cmd\git.exe"
    )
    check = subprocess.run(
        [str(git), "-C", str(root), "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        text=True,
    )
    if check.returncode:
        return {"root": str(root), "is_git": False}
    log = subprocess.run(
        [
            str(git),
            "-C",
            str(root),
            "log",
            "--date=iso-strict",
            "--pretty=format:%H%x09%ad%x09%an%x09%s",
            "--name-status",
            "--all",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    status = subprocess.run(
        [str(git), "-C", str(root), "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
    )
    return {
        "root": str(root),
        "is_git": True,
        "log": log.stdout,
        "status": status.stdout,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    TEXT_OUT.mkdir(parents=True, exist_ok=True)
    all_files = sorted(
        (
            path
            for root in (PA1, PA2)
            for path in root.rglob("*")
            if path.is_file() and not is_skipped(path)
        ),
        key=lambda path: str(path).lower(),
    )
    pdfs = [path for path in all_files if path.suffix.lower() == ".pdf"]
    images = [path for path in all_files if path.suffix.lower() in IMAGE_EXTENSIONS]
    texts = [path for path in all_files if path.suffix.lower() in TEXT_EXTENSIONS]

    pdfs_data = [pdf_record(path) for path in pdfs]
    images_data = [image_record(path) for path in images]
    texts_data = []
    for path in texts:
        try:
            content = path.read_text(encoding="utf-8")
            encoding = "utf-8"
        except UnicodeDecodeError:
            content = path.read_text(encoding="utf-8-sig", errors="replace")
            encoding = "utf-8-sig/replace"
        texts_data.append(
            {
                "path": str(path),
                "relative": relative_label(path),
                "size": path.stat().st_size,
                "sha256": sha256(path),
                "encoding": encoding,
                "content": content,
            }
        )

    inventory = []
    for path in all_files:
        stat = path.stat()
        inventory.append(
            {
                "relative": relative_label(path),
                "path": str(path),
                "extension": path.suffix.lower(),
                "size": stat.st_size,
                "modified": stat.st_mtime,
            }
        )
    with (OUT / "file-inventory.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=inventory[0].keys())
        writer.writeheader()
        writer.writerows(inventory)

    duplicates: dict[str, list[str]] = {}
    for record in images_data:
        duplicates.setdefault(record["sha256"], []).append(record["path"])
    duplicate_groups = [paths for paths in duplicates.values() if len(paths) > 1]

    audit = {
        "counts": {
            "files": len(all_files),
            "pdfs": len(pdfs_data),
            "pdf_pages": sum(len(item["pages"]) for item in pdfs_data),
            "images": len(images_data),
            "texts": len(texts_data),
            "exact_duplicate_image_groups": len(duplicate_groups),
        },
        "pdfs": pdfs_data,
        "images": images_data,
        "texts": texts_data,
        "duplicate_image_groups": duplicate_groups,
        "git": [git_record(PA1), git_record(PA2)],
    }
    (OUT / "audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(audit["counts"], indent=2))
    print(f"Audit: {OUT / 'audit.json'}")


if __name__ == "__main__":
    main()
