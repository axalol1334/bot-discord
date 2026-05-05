import discord
from discord.ext import commands, tasks
import os

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1501246653779415150  # <-- remplace par ton salon

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    send_alive_message.start()  # lance la boucle

@tasks.loop(minutes=1)
async def send_alive_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("je fonctionne ✅")

bot.run(os.getenv("TOKEN"))
