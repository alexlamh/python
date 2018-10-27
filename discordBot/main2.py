import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
TOKEN = "NDcyNTc1MDcwOTMwNDY4ODY0.DoxqQA.5yev1BulYMNRI_7_uAjaEyyMWo8"

@client.event
async def on_ready():
    print("Bot online e conectado no Discord")

message = 'Hi'

@client.event
async def send(message):
    await client.send_message(client.get_channel("427953907860242444"), message)

@client.command()
async def send(*, message):
    global target_channel
    await client.send_message(client.get_channel('428606773474230272'), message)

client.run(TOKEN)
