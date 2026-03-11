#!/usr/bin/env python3
"""
Update existing vectors.json with metadata from frontmatter.
Run after adding frontmatter to markdown files.
"""

import json
import os
import sys
from pathlib import Path

# Add parent directory to path to import rag
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.rag import parse_frontmatter

VECTORS_PATH = Path(__file__).parent.parent / "data" / "vectors.json"
KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"

def update_vectors_with_metadata():
    if not VECTORS_PATH.exists():
        print(f"❌ {VECTORS_PATH} not found.")
        return False

    print(f"📖 Loading existing vectors from {VECTORS_PATH}...")
    with open(VECTORS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    print(f"🔍 Processing {len(chunks)} chunks...")

    updated = 0
    errors = 0

    for i, chunk in enumerate(chunks):
        source = chunk.get("source", "")
        if not source:
            continue

        # Build absolute path to source markdown file
        source_path = KNOWLEDGE_DIR / source.replace("\\", "/")

        if not source_path.exists():
            # Try to find file with different case (should not happen)
            print(f"⚠️  Source file not found: {source_path}")
            errors += 1
            continue

        # Read file and parse frontmatter
        try:
            with open(source_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"⚠️  Failed to read {source_path}: {e}")
            errors += 1
            continue

        metadata, _ = parse_frontmatter(content)

        # Check if metadata already exists and is different
        existing_metadata = chunk.get("metadata", {})
        if existing_metadata == metadata:
            # Already up-to-date
            continue

        chunk["metadata"] = metadata
        updated += 1

        if (i + 1) % 100 == 0:
            print(f"  Processed {i+1} chunks...")

    if updated > 0:
        # Write updated vectors (minified — no indent, no embeddings stored inline)
        print(f"💾 Writing updated vectors with metadata for {updated} chunks...")
        with open(VECTORS_PATH, "w", encoding="utf-8") as f:
            json.dump(chunks, f)
        print(f"✅ Updated {updated} chunks with metadata.")
    else:
        print("✅ No updates needed; metadata already present.")

    if errors:
        print(f"⚠️  Encountered {errors} errors.")

    return True


if __name__ == "__main__":
    update_vectors_with_metadata()