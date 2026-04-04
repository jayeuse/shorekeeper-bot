#!/usr/bin/env python3
"""
Script to add YAML frontmatter to markdown knowledge files.
Run from project root: python add_frontmatter.py
"""

import os
import sys
import shutil
import yaml
from pathlib import Path
from typing import Any, Dict, List, cast

REPO_ROOT = Path(__file__).parent.parent
KNOWLEDGE_DIR = REPO_ROOT / "knowledge"
BACKUP_DIR = REPO_ROOT / "knowledge_backups"
EXCLUDE_DIRS = {"references", ".git", "__pycache__"}


def _ensure_list(metadata: Dict[str, Any], key: str) -> None:
    v = metadata.get(key)
    if v is None:
        metadata[key] = []
        return
    if isinstance(v, str):
        metadata[key] = [v]
        return
    if not isinstance(v, list):
        try:
            metadata[key] = list(v)
        except Exception:
            metadata[key] = [str(v)]


def get_metadata_from_path(filepath):
    """Generate metadata based on file path relative to knowledge/."""
    rel_path = filepath.relative_to(KNOWLEDGE_DIR)
    parts = rel_path.parts
    filename = parts[-1]
    name_no_ext = filename[:-3]  # Remove .md

    metadata: Dict[str, Any] = {
        "version": "1.0.0",
        "chunk_strategy": "heading_based",
        "source_file": str(rel_path),
    }

    # Determine document type and additional metadata
    if parts[0] == "characters":
        if len(parts) >= 3:
            group = parts[1]  # e.g., black_shores
            char_dir = parts[2]  # character directory name
            character = char_dir.replace("_", " ").title()

            metadata["character"] = character
            metadata["group"] = group.replace("_", " ").title()

            if name_no_ext.endswith("_character"):
                metadata["document_type"] = "character_profile"
                metadata["importance"] = "medium"
                _ensure_list(metadata, "tags")
                tags = cast(List[str], metadata["tags"])
                tags.extend(["character", "profile"])
            elif name_no_ext.endswith("_kit"):
                metadata["document_type"] = "character_kit"
                metadata["importance"] = "high"
                _ensure_list(metadata, "tags")
                tags = cast(List[str], metadata["tags"])
                tags.extend(["character", "kit", "combat"])
            elif name_no_ext.endswith("_story"):
                metadata["document_type"] = "character_story"
                metadata["importance"] = "medium"
                _ensure_list(metadata, "tags")
                tags = cast(List[str], metadata["tags"])
                tags.extend(["character", "story", "lore"])
            else:
                metadata["document_type"] = "character_other"
                metadata["importance"] = "low"

        else:
            # Top-level character files (e.g., voice_actors.txt but we skip .md)
            metadata["document_type"] = "character_reference"
            metadata["importance"] = "low"

    elif parts[0] == "lore":
        if len(parts) >= 2 and parts[1] == "regions":
            if len(parts) >= 3:
                region = parts[2]  # e.g., rinascita
                metadata["region"] = region.replace("_", " ").title()

                # Check for quests subdirectory
                if "quests" in parts:
                    metadata["document_type"] = "quest"
                    metadata["importance"] = "low"
                    # Determine quest type from filename
                    if "_mq_" in filename:
                        if "_prologue" in filename:
                            metadata["quest_type"] = "prologue"
                        elif "_act" in filename:
                            metadata["quest_type"] = "act"
                        elif "_seg" in filename:
                            metadata["quest_type"] = "segment"
                        elif "_ic" in filename:
                            metadata["quest_type"] = "interlude"
                        elif "_themes" in filename:
                            metadata["quest_type"] = "thematic_analysis"
                        else:
                            metadata["quest_type"] = "chapter"
                    _ensure_list(metadata, "tags")
                    tags = cast(List[str], metadata["tags"])
                    tags.extend(["lore", "quest", region])
                else:
                    # Region story/places files
                    if "_story" in filename:
                        metadata["document_type"] = "region_story"
                        metadata["importance"] = "medium"
                        _ensure_list(metadata, "tags")
                        tags = cast(List[str], metadata["tags"])
                        tags.extend(["lore", "region", "story"])
                    elif "_places" in filename:
                        metadata["document_type"] = "region_places"
                        metadata["importance"] = "medium"
                        _ensure_list(metadata, "tags")
                        tags = cast(List[str], metadata["tags"])
                        tags.extend(["lore", "region", "geography"])
                    elif "_territories" in filename:
                        metadata["document_type"] = "region_territories"
                        metadata["importance"] = "medium"
                        _ensure_list(metadata, "tags")
                        tags = cast(List[str], metadata["tags"])
                        tags.extend(["lore", "region", "geography"])
                    else:
                        metadata["document_type"] = "region_other"
                        metadata["importance"] = "low"
            else:
                # Top-level lore files (e.g., history.md, world.md)
                metadata["document_type"] = "lore_general"
                metadata["importance"] = "medium"
                _ensure_list(metadata, "tags")
                tags = cast(List[str], metadata["tags"])
                tags.append("lore")
        else:
            metadata["document_type"] = "lore"
            metadata["importance"] = "medium"

    elif parts[0] == "personalization":
        if "personality" in filename:
            metadata["document_type"] = "personality"
            metadata["importance"] = "high"
            _ensure_list(metadata, "tags")
            tags = cast(List[str], metadata["tags"])
            tags.extend(["shorekeeper", "personality"])
        elif "backstory" in filename:
            metadata["document_type"] = "backstory"
            metadata["importance"] = "high"
            _ensure_list(metadata, "tags")
            tags = cast(List[str], metadata["tags"])
            tags.extend(["shorekeeper", "backstory"])
        elif "relationships" in filename:
            metadata["document_type"] = "relationships"
            metadata["importance"] = "medium"
            _ensure_list(metadata, "tags")
            tags = cast(List[str], metadata["tags"])
            tags.extend(["shorekeeper", "relationships"])
        else:
            metadata["document_type"] = "personalization"
            metadata["importance"] = "medium"

    elif parts[0] == "systems":
        metadata["document_type"] = "game_mechanics"
        metadata["importance"] = "medium"
        _ensure_list(metadata, "tags")
        tags = cast(List[str], metadata["tags"])
        tags.extend(["systems", "mechanics"])

    else:
        metadata["document_type"] = "unknown"
        metadata["importance"] = "low"

    # Ensure tags is a list
    if "tags" not in metadata:
        metadata["tags"] = []

    # Remove any duplicate tags
    if metadata["tags"]:
        metadata["tags"] = list(dict.fromkeys(metadata["tags"]))

    return metadata


def has_frontmatter(content):
    """Check if content already has YAML frontmatter."""
    return content.startswith("---\n") and "\n---\n" in content[4:]


def add_frontmatter_to_file(filepath, dry_run=False, skip_backup=False):
    """Add YAML frontmatter to a markdown file if not present."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if has_frontmatter(content):
        print(f"✓ Already has frontmatter: {filepath}")
        return False

    metadata = get_metadata_from_path(filepath)

    # Generate YAML frontmatter
    frontmatter = yaml.dump(metadata, default_flow_style=False, sort_keys=False)
    new_content = f"---\n{frontmatter}---\n\n{content}"

    if dry_run:
        print(f"DRY RUN: Would update {filepath}")
        print(f"  Metadata: {metadata}")
        return True

    # Backup original file to knowledge_backups/ (optional)
    if not skip_backup:
        try:
            # Get relative path from knowledge directory
            rel_path = filepath.relative_to(KNOWLEDGE_DIR)
            # Construct backup path preserving directory structure
            backup_path = BACKUP_DIR / rel_path.with_suffix(rel_path.suffix + ".bak")
            # Ensure parent directory exists
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            # Copy file
            shutil.copy2(filepath, backup_path)
        except Exception as e:
            print(f"⚠️  Failed to create backup for {filepath}: {e}")

    # Write new content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✓ Added frontmatter to: {filepath}")
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Add YAML frontmatter to knowledge markdown files.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be changed without writing")
    parser.add_argument("--skip-backup", action="store_true", help="Skip creating backups in knowledge_backups/ directory")
    args = parser.parse_args()

    md_files = []
    for root, dirs, files in os.walk(KNOWLEDGE_DIR):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]

        for file in files:
            if file.endswith(".md") and file != "FORMAT_GUIDE.md":
                md_files.append(Path(root) / file)

    print(f"Found {len(md_files)} markdown files in knowledge/")

    updated_count = 0
    for filepath in md_files:
        try:
            if add_frontmatter_to_file(filepath, dry_run=args.dry_run, skip_backup=args.skip_backup):
                updated_count += 1
        except Exception as e:
            print(f"✗ Error processing {filepath}: {e}")

    print(f"\n{'DRY RUN: ' if args.dry_run else ''}Updated {updated_count} files")
    if not args.dry_run and updated_count > 0 and not args.skip_backup:
        print(f"Note: Original files backed up to {BACKUP_DIR}")


if __name__ == "__main__":
    main()