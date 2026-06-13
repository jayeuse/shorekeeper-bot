import sys
from pathlib import Path

# Add brain directory to path so we can import services
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services.rag import RAG


def main():
    print("🚀 Manual Knowledge Base Rebuild Initiated")
    print("=" * 40)

    rag = RAG()
    try:
        rag.build()
        print("\n" + rag.get_manifest())
        print("\n✅ Successfully rebuilt and saved vectors.json and embeddings.npz")
    except Exception as e:
        print(f"\n❌ Error during build: {e}")
        if "ConnectionError" in str(e):
            print(
                "💡 Tip: Make sure your embedding provider is reachable before starting the rebuild."
            )
            print("   For llama.cpp, start a server that exposes /v1/embeddings.")
        sys.exit(1)


if __name__ == "__main__":
    main()
