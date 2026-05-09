#!/usr/bin/env python3
"""Read-only folder inventory for the folder-librarian skill."""

from __future__ import annotations

import argparse
import json
import os
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


VIDEO_EXTENSIONS = {
    ".avi",
    ".flv",
    ".m4v",
    ".mov",
    ".mp4",
    ".mpeg",
    ".mpg",
    ".wmv",
}

IMAGE_EXTENSIONS = {
    ".gif",
    ".heic",
    ".jpeg",
    ".jpg",
    ".png",
    ".tif",
    ".tiff",
    ".webp",
}

ARCHIVE_EXTENSIONS = {
    ".7z",
    ".bz2",
    ".gz",
    ".rar",
    ".tar",
    ".tgz",
    ".zip",
}

DOCUMENT_EXTENSIONS = {
    ".csv",
    ".doc",
    ".docx",
    ".html",
    ".md",
    ".pdf",
    ".ppt",
    ".pptm",
    ".pptx",
    ".txt",
    ".xls",
    ".xlsm",
    ".xlsx",
}


def human_size(num_bytes: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(num_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(size)} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{num_bytes} B"


def rel(path: Path, root: Path) -> str:
    try:
        value = path.relative_to(root)
    except ValueError:
        value = path
    text = str(value)
    return "." if text == "." else text


def is_screenshot(path: Path) -> bool:
    name = path.name.lower()
    return path.suffix.lower() in IMAGE_EXTENSIONS and (
        "screenshot" in name or "screen shot" in name
    )


def add_parent_sizes(folder_sizes: dict[Path, int], root: Path, file_path: Path, size: int) -> None:
    parent = file_path.parent
    while True:
        folder_sizes[parent] += size
        if parent == root:
            break
        try:
            parent = parent.parent
        except RuntimeError:
            break


def inventory(root: Path, top: int) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.exists():
        raise FileNotFoundError(f"Folder does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Not a folder: {root}")

    extension_counts: Counter[str] = Counter()
    top_level_counts: Counter[str] = Counter()
    duplicate_names: dict[str, list[str]] = defaultdict(list)
    folder_sizes: dict[Path, int] = defaultdict(int)
    largest_files: list[tuple[int, Path]] = []
    root_files: list[Path] = []
    cleanup_candidates: Counter[str] = Counter()
    unreadable: list[str] = []
    total_files = 0
    total_dirs = 0
    total_size = 0

    for current, dirnames, filenames in os.walk(root, followlinks=False):
        current_path = Path(current)
        dirnames[:] = [name for name in dirnames if not (current_path / name).is_symlink()]
        total_dirs += len(dirnames)

        for filename in filenames:
            file_path = current_path / filename
            if file_path.is_symlink():
                cleanup_candidates["symlinks_skipped"] += 1
                continue

            try:
                stat = file_path.stat()
            except OSError as exc:
                unreadable.append(f"{rel(file_path, root)} ({exc})")
                continue

            size = stat.st_size
            total_files += 1
            total_size += size
            add_parent_sizes(folder_sizes, root, file_path, size)

            suffix = file_path.suffix.lower() or "[no extension]"
            extension_counts[suffix] += 1

            relative = file_path.relative_to(root)
            first_part = relative.parts[0] if relative.parts else file_path.name
            top_level_counts[first_part] += 1
            if len(relative.parts) == 1:
                root_files.append(file_path)

            duplicate_names[file_path.name.lower()].append(rel(file_path, root))
            largest_files.append((size, file_path))

            lower_name = file_path.name.lower()
            if lower_name == ".ds_store":
                cleanup_candidates[".DS_Store"] += 1
            if suffix == ".partial" or lower_name.endswith(".partial"):
                cleanup_candidates["partial_downloads"] += 1
            if suffix in VIDEO_EXTENSIONS:
                cleanup_candidates["videos"] += 1
            if suffix in ARCHIVE_EXTENSIONS:
                cleanup_candidates["archives"] += 1
            if is_screenshot(file_path):
                cleanup_candidates["screenshots"] += 1

    largest_files = sorted(largest_files, reverse=True)[:top]
    largest_folders = sorted(
        ((size, path) for path, size in folder_sizes.items() if path != root),
        reverse=True,
    )[:top]

    duplicate_report = {
        name: paths
        for name, paths in sorted(duplicate_names.items())
        if len(paths) > 1
    }

    risk_flags = build_risk_flags(
        total_files=total_files,
        root_files=len(root_files),
        extension_counts=extension_counts,
        duplicate_count=len(duplicate_report),
        cleanup_candidates=cleanup_candidates,
    )

    return {
        "root": str(root),
        "totals": {
            "files": total_files,
            "folders": total_dirs,
            "size_bytes": total_size,
            "size_human": human_size(total_size),
            "root_level_files": len(root_files),
        },
        "extensions": extension_counts.most_common(),
        "top_level_file_counts": top_level_counts.most_common(top),
        "largest_files": [
            {"size_bytes": size, "size_human": human_size(size), "path": rel(path, root)}
            for size, path in largest_files
        ],
        "largest_folders": [
            {"size_bytes": size, "size_human": human_size(size), "path": rel(path, root)}
            for size, path in largest_folders
        ],
        "duplicate_filenames": {
            "count": len(duplicate_report),
            "examples": dict(list(duplicate_report.items())[:top]),
        },
        "cleanup_candidates": cleanup_candidates.most_common(),
        "risk_flags": risk_flags,
        "unreadable": unreadable[:top],
    }


def build_risk_flags(
    *,
    total_files: int,
    root_files: int,
    extension_counts: Counter[str],
    duplicate_count: int,
    cleanup_candidates: Counter[str],
) -> list[str]:
    flags: list[str] = []

    if root_files >= 25:
        flags.append("Many root-level files; consider a Start Here index and top-level triage.")
    if duplicate_count:
        flags.append("Duplicate filenames exist; compare content before deleting anything.")
    if cleanup_candidates.get("partial_downloads", 0):
        flags.append("Partial downloads found; quarantine or review before cleanup.")
    if cleanup_candidates.get(".DS_Store", 0):
        flags.append("macOS .DS_Store files found; safe cleanup candidates after approval.")
    if cleanup_candidates.get("videos", 0) >= 10:
        flags.append("Large video/training archive likely; keep media separate from reference docs.")
    if cleanup_candidates.get("archives", 0):
        flags.append("Archive files found; preserve original bundles unless deletion is approved.")

    doc_exts = sum(count for ext, count in extension_counts.items() if ext in DOCUMENT_EXTENSIONS)
    image_exts = sum(count for ext, count in extension_counts.items() if ext in IMAGE_EXTENSIONS)
    video_exts = sum(count for ext, count in extension_counts.items() if ext in VIDEO_EXTENSIONS)
    if len(extension_counts) >= 8 and total_files >= 50:
        flags.append("Mixed file types; use organization by retrieval need, not by extension alone.")
    if doc_exts and (image_exts or video_exts):
        flags.append("Mixed documents and media; read local tool guidance before conversion work.")

    return flags


def print_text_report(data: dict[str, Any]) -> None:
    totals = data["totals"]
    print(f"Folder: {data['root']}")
    print(
        "Totals: "
        f"{totals['files']} files, {totals['folders']} folders, "
        f"{totals['size_human']}, {totals['root_level_files']} root-level files"
    )

    print("\nTop extensions:")
    for ext, count in data["extensions"][:15]:
        print(f"  {ext}: {count}")

    print("\nTop-level file counts:")
    for name, count in data["top_level_file_counts"]:
        print(f"  {name}: {count}")

    print("\nLargest folders:")
    for item in data["largest_folders"]:
        print(f"  {item['size_human']}: {item['path']}")

    print("\nLargest files:")
    for item in data["largest_files"]:
        print(f"  {item['size_human']}: {item['path']}")

    duplicates = data["duplicate_filenames"]
    print(f"\nDuplicate filenames: {duplicates['count']}")
    for name, paths in duplicates["examples"].items():
        print(f"  {name}: {len(paths)} copies")

    print("\nCleanup candidates:")
    if data["cleanup_candidates"]:
        for name, count in data["cleanup_candidates"]:
            print(f"  {name}: {count}")
    else:
        print("  none flagged")

    print("\nRisk flags:")
    if data["risk_flags"]:
        for flag in data["risk_flags"]:
            print(f"  - {flag}")
    else:
        print("  none")

    if data["unreadable"]:
        print("\nUnreadable examples:")
        for item in data["unreadable"]:
            print(f"  {item}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a read-only inventory of a folder.")
    parser.add_argument("folder", help="Folder to inspect")
    parser.add_argument("--top", type=int, default=12, help="Number of examples to show")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of text")
    args = parser.parse_args()

    data = inventory(Path(args.folder), max(1, args.top))
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print_text_report(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
