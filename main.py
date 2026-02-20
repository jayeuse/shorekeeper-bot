from core.bot import bot
from core.config import DISCORD_TOKEN
from services.rag import RAG

print("🔄 Building knowledge base...")
rag = RAG()
rag.build()

bot.run(DISCORD_TOKEN)