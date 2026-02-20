from services.rag import RAG

print("Initializing RAG for Phrolova Test...")
rag = RAG()
rag.load()  # Load existing vectors, don't rebuild
print(f"Loaded {len(rag.chunks)} chunks.")

queries = [
    "What specific role did Phrolova play in Act VII: Dreamcatchers in the Secret Gardens?",
    "Describe the 'Lost Beyond' or 'Secret Gardens' location.",
    "How does Phrolova's 'Dream Weaving' ability work?",
    "What is the connection between Phrolova and the Threnodian of War?",
    "What did Phrolova say to Fenrico during their confrontation?",
    "What is Phrolova's history with the village of Ostina?",
]

print("\n--- Testing Phrolova Lore Retrieval ---\n")
for q in queries:
    print(f"🔹 Query: {q}")
    results = rag.search(q, top_k=3)
    for i, r in enumerate(results):
        print(f"   {i+1}. [{r['score']:.4f}] {r['heading']} ({r['source']})")
        # Print a snippet of the text to verify content
        snippet = r['text'][:100].replace('\n', ' ') + "..."
        print(f"      \"{snippet}\"")
    print("-" * 50)
