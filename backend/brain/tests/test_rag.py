from services.rag import RAG

rag = RAG()
rag.build()
print()

queries = [

    # All Character Queries (2-3 per character)
    # [Shorekeeper]
    "What is the Black Shores organization?",
    "How does Shorekeeper's healing work?",
    "What is Shorekeeper's relationship with the Rover?",
    
    # [Camellya]
    "Who is Camellya?",
    "Explain Camellya's combat kit and element.",
    "What is Camellya's backstory?",

    # [Cartethyia]
    "What weapons does Cartethyia use?",
    "Tell me about Cartethyia's personality and ideals.",

    # [Galbrena]
    "What is Galbrena's role in combat?",
    "Describe Galbrena's relationship with the Tethys System.",
    
    # [Zani]
    "How does Zani's Inferno Mode work?",
    "What are Zani's best team compositions?",
    
    # [Cantarella]
    "Explain Cantarella's 'Mirage State' mechanic.",
    "What is Cantarella's relationship with Phrolova?",
    
    # [Carlotta]
    "How do I use Carlotta's 'Tinted Crystal' mechanic?",
    "What is the best weapon for Carlotta?",

    # [Lupa]
    "What is Lupa's 'Wolf Spirit' mechanic?",
    "Tell me about Lupa's backstory and origin.",

    # [Phrolova]
    "Who is Phrolova?",
    "Explain Phrolova's Hecate coordinated attacks.",

    # [Iuno]
    "What is Iuno's role in a team?",
    "Describe Iuno's personality.",

    # [Augusta]
    "Who is Augusta?",
    "What element does Augusta use?",
    
    # [Chisa]
    "Who is Chisa?",
    "What makes Chisa unique?",

    # General Game Mechanics (4 queries)
    "How does the 'Concerto Energy' system work?",
    "What is the difference between Resonance Skill and Resonance Liberation?",
    "Explain the 'Vibration Strength' mechanic on bosses.",
    "How do Outro Skills trigger?",

    # General Lore & World Knowledge (4 queries)
    "What is the Lament in Wuthering Waves?",
    "Tell me about the history of the Black Shores.",
    "What are 'Echoes' and how are they formed?",
    "Who are the Threnodians?",

    # Personalization & System Prompt Checks (4 queries)
    "What is your personality like, Shorekeeper?",
    "Do you have feelings for the Rover?",
    "How would you describe your voice and manner of speaking?",
    "What is your philosophy on 'choice' and 'fate'?"
]

for q in queries:
    results = rag.search(q, top_k=5)
    print(f'🔍 "{q}"')
    for r in results:
        print(f'   [{r["score"]:.3f}] {r["source"]} → {r["heading"]}')
    print()
