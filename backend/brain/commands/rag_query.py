#!/usr/bin/env python3
"""Interactive RAG query utility.

Usage:
    python commands/rag_query.py

Enter queries to search the knowledge base. Type '/exit' to quit.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services.rag import RAG


def main() -> None:
    rag = RAG()
    if not rag.load():
        print("❌ Failed to load knowledge base. Exiting.")
        return

    print("🔍 RAG Query Tool (type '/exit' to quit)")
    print("=" * 60)

    while True:
        try:
            query = input("\n📝 Enter query: ").strip()
        except EOFError:
            print("\n👋 Goodbye!")
            break

        if query.lower() == "/exit":
            print("👋 Goodbye!")
            break

        if not query:
            print("⚠️  Empty query. Try again.")
            continue

        results = rag.search(query, top_k=5)

        if not results:
            print("❌ No results found.")
            continue

        print(f"\n✅ Found {len(results)} results for: {query}")
        print("-" * 60)
        for i, result in enumerate(results, 1):
            print(
                f"{i}. [{result['score']:.4f}] {result['source']} → {result['heading']}"
            )
        print("-" * 60)


if __name__ == "__main__":
    main()
