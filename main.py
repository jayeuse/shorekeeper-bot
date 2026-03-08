from core.bot import bot
from core.config import DISCORD_TOKEN
from services.rag import RAG
import sys

print("🔄 Building knowledge base...")
rag = RAG()
rag.build()

if DISCORD_TOKEN is None:
    sys.exit("ERROR: DISCORD_TOKEN is not set. Add it to .env.local or environment variables.")


bot.run(DISCORD_TOKEN)