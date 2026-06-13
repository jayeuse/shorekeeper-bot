import sys

from core.bot import bot
from core.config import DISCORD_TOKEN
from services.rag import RAG

print("🔄 Loading knowledge base...")
rag = RAG()
if not rag.load():
    print("⚠️  No existing knowledge base found!")
    print("👉 Please run: python brain/commands/rebuild_index.py")
    # We don't exit here so the bot can still start, but it won't have lore context.
else:
    print("\n" + rag.get_manifest() + "\n")

if DISCORD_TOKEN is None:
    sys.exit("ERROR: DISCORD_TOKEN is not set. Add it to .env.local or environment variables.")


bot.run(DISCORD_TOKEN)
