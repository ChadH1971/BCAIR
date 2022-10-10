# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv("DISCORD_GUILD")

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    GUILD = discord.utils.get(client.guilds, name=guild)

    print(f'{client.user} is connected to {GUILD.name} (id: {GUILD.id})')


client.run(token)
