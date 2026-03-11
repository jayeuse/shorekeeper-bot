#!/usr/bin/env python3
"""
Move .bak backup files from knowledge/ to knowledge_backups/ preserving directory structure.
"""

import os
import shutil
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"
BACKUP_DIR = Path(__file__).parent.parent / "knowledge_backups"

def move_backups():
    if not KNOWLEDGE_DIR.exists():
        print(f"❌ Knowledge directory not found: {KNOWLEDGE_DIR}")
        return False

    BACKUP_DIR.mkdir(exist_ok=True)

    # Find all .bak files
    bak_files = list(KNOWLEDGE_DIR.rglob("*.bak"))
    print(f"Found {len(bak_files)} backup files in knowledge/")

    moved = 0
    errors = 0

    for bak_file in bak_files:
        # Get relative path from knowledge directory
        rel_path = bak_file.relative_to(KNOWLEDGE_DIR)

        # Construct destination path in backup directory
        dest_path = BACKUP_DIR / rel_path

        # Ensure destination directory exists
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            # Move the file
            shutil.move(str(bak_file), str(dest_path))
            moved += 1
            if moved % 10 == 0:
                print(f"  Moved {moved} files...")
        except Exception as e:
            print(f"❌ Error moving {bak_file}: {e}")
            errors += 1

    print(f"\n✅ Moved {moved} backup files to {BACKUP_DIR}")
    if errors:
        print(f"⚠️  {errors} errors occurred")

    # Clean up empty directories in knowledge/
    print("\n🧹 Cleaning up empty directories in knowledge/...")
    cleaned = 0
    for root, dirs, files in os.walk(KNOWLEDGE_DIR, topdown=False):
        for dir_name in dirs:
            dir_path = Path(root) / dir_name
            try:
                if not any(dir_path.iterdir()):
                    dir_path.rmdir()
                    cleaned += 1
            except Exception:
                pass

    if cleaned:
        print(f"  Removed {cleaned} empty directories")

    return True

if __name__ == "__main__":
    move_backups()