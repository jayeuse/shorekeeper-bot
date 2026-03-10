import json
import os
from collections import defaultdict, Counter
from tabulate import tabulate

VECTORS_PATH = os.path.join(os.path.dirname(__file__), "data", "vectors.json")

def analyze_knowledge():
    if not os.path.exists(VECTORS_PATH):
        print(f"❌ No vector store found at {VECTORS_PATH}")
        print("   Run 'python main.py' to build the knowledge base first.")
        return

    try:
        with open(VECTORS_PATH, "r", encoding="utf-8") as f:
            chunks = json.load(f)
    except Exception as e:
        print(f"❌ Failed to load vectors.json: {e}")
        return

    print(f"📚 Total Knowledge Chunks: {len(chunks)}\n")

    # Categories
    stats = {
        "characters": defaultdict(int),
        "regions": defaultdict(int),
        "lore": defaultdict(int),
        "personalization": defaultdict(int),
        "other": defaultdict(int)
    }

    # Analyze chunks
    for chunk in chunks:
        source = chunk.get("source", "").replace("\\", "/")
        parts = source.split("/")
        
        if not parts:
            continue

        category = parts[0]
        
        if category == "characters":
            # Handle nested structure: characters/{region}/{character}/...
            # e.g. characters/black_shores/shorekeeper/shorekeeper_story.md
            if len(parts) > 2:
                # The character name is likely the third part
                char_name = parts[2].replace("_", " ").title()
                # Special handling if the part ends with .md (file directly in region folder)
                if char_name.endswith(".Md"): 
                    # If it's a file, maybe group by file name or region
                    stats["characters"][char_name.replace(".Md", "")] += 1
                else:
                    stats["characters"][char_name] += 1
            elif len(parts) > 1:
                # e.g. characters/old_character_file.md
                name = parts[1]
                if name.endswith(".md") or name.endswith(".txt"):
                    stats["characters"]["_Misc Files"] += 1
                else:
                    char_name = name.replace("_", " ").title()
                    stats["characters"][char_name] += 1
            else:
                stats["other"]["misc_characters"] += 1
                
        elif category == "lore":
            # format: knowledge/lore/regions/{region}/... or knowledge/lore/{file}
            if len(parts) > 2 and parts[1] == "regions":
                region_name = parts[2].replace("_", " ").title()
                stats["regions"][region_name] += 1
            else:
                # General lore files
                filename = os.path.splitext(parts[-1])[0].replace("_", " ").title()
                stats["lore"][filename] += 1
                
        elif category == "personalization":
            filename = os.path.splitext(parts[-1])[0].replace("_", " ").title()
            stats["personalization"][filename] += 1
            
        else:
            # Everything else (dialogues, wiki, etc)
            stats["other"][category.title()] += 1

    # Print Report
    print_section("Characters", stats["characters"])
    print_section("Regions", stats["regions"])
    print_section("General Lore", stats["lore"])
    print_section("Personalization", stats["personalization"])
    print_section("Other Categories", stats["other"])

def print_section(title, data):
    if not data:
        return
        
    print(f"🔹 {title}")
    table_data = [[k, v] for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)]
    print(tabulate(table_data, headers=["Entity/File", "Chunks"], tablefmt="simple"))
    print()

if __name__ == "__main__":
    analyze_knowledge()
