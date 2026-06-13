import discord
from handlers.message import on_message as handle_message

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot is logged in as {bot.user} (ID: {bot.user.id})")
    print("🚀 Shorekeeper is ready to receive messages.")

@bot.event
async def on_message(msg):
    await handle_message(bot, msg)
