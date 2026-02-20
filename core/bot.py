import discord
from handlers.message import on_message as handle_message

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_message(msg):
    await handle_message(bot, msg)
