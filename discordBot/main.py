import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
TOKEN = "NDcyNTA2NzgwMDA2NzQ0MDY1.Dj0Ypg.sXh4q2rX4tbCq8L-QMsoWBS8z3Y"

@client.event
async def on_ready():
    print("Bot online e conectado no Discord")

@client.event
async def on_message(message):
    if message.content.lower().startswith('!ping'):
        await client.send_message(message.channel, "Pong!")
    if message.content.lower().startswith('!say'):
        if message.author.id == "170258054003032075":
            await client.send_message(message.channel, "Hi!")
        else:
            await client.send_message(message.channel, "You do not have permission!")

    #Elite 448110039039868928
    if "428007003697446923" in [role.id for role in message.author.roles]:
        if message.content.lower().startswith('!adm'):
            await client.send_message(message.channel, "You are adm")

    if message.content.lower().startswith('p!elite'):
        if "448110039039868928" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "You are Elite")
        else:
            await client.send_message(message.channel, "You are **NOT** Elite")




client.run(TOKEN)