import discord
from handlers.message import on_message as handle_message
from handlers.search_command import register_search_command

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)
register_search_command(tree)
_command_tree_synced = False


@bot.event
async def on_ready():
    global _command_tree_synced
    if not _command_tree_synced:
        await tree.sync()
        _command_tree_synced = True
    print(f"✅ Bot is logged in as {bot.user} (ID: {bot.user.id})")
    print("🚀 Shorekeeper is ready to receive messages.")


@bot.event
async def on_message(msg):
    await handle_message(bot, msg)
