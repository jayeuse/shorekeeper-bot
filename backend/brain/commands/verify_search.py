import asyncio
import sys
from pathlib import Path

# Add brain directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.config import SEARCH_BASE_URL, SEARCH_MAX_RESULTS, SEARCH_PROVIDER
from services.search import SearchError, build_search_provider


async def verify() -> None:
    print("🔍 Testing Search Connectivity...")
    print("=" * 40)

    try:
        provider = build_search_provider()
        query = "latest Wuthering Waves update"
        print(
            f"📡 Sending test request via provider={SEARCH_PROVIDER} "
            f"to {SEARCH_BASE_URL} with limit={SEARCH_MAX_RESULTS}..."
        )

        bundle = await provider.search(query, SEARCH_MAX_RESULTS)
        print(f"\n✅ Search query completed for: {bundle.query}")
        print(f"📊 Results returned: {len(bundle.results)}")

        for index, result in enumerate(bundle.results[:3], start=1):
            print(f"\n[{index}] {result.title}")
            print(f"    Source: {result.source}")
            print(f"    URL: {result.url}")
            if result.published_at:
                print(f"    Published: {result.published_at}")
            if result.snippet:
                print(f"    Snippet: {result.snippet}")

        if not bundle.results:
            print("\n⚠️ Search endpoint responded but returned no results.")

        print("\n✅ Verification Complete!")
    except SearchError as exc:
        print(f"\n❌ Search Verification Failed: {exc}")
        sys.exit(1)
    except Exception as exc:
        print(f"\n❌ Unexpected Search Failure: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(verify())
