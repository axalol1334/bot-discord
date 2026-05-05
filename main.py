import discord
from discord.ext import commands, tasks
import os
import asyncio

# --- CONFIG ---
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 123456789012345678  # <-- remplace par ton salon

# --- INTENTS ---
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# --- READY EVENT ---
@bot.event
async def on_ready():
    print(f"[INFO] Connecté en tant que {bot.user}")

    if not send_alive_message.is_running():
        send_alive_message.start()
        print("[INFO] boucle démarrée")

# --- LOOP MESSAGE ---
@tasks.loop(minutes=1)
async def send_alive_message():
    try:
        print("[DEBUG] tentative d'envoi du message...")

        channel = await bot.fetch_channel(CHANNEL_ID)

        await channel.send("je fonctionne ✅")

        print("[SUCCESS] message envoyé avec succès")

    except Exception as e:
        print(f"[ERROR] échec envoi message : {e}")

# --- COMMANDE TEST ---
@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

# --- RUN BOT ---
bot.run(TOKEN)

@app.route('/')
def home():
    return "OK", 200
