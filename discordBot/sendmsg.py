import discord
import asyncio

client = discord.Client()
token = "NDcyNTc1MDcwOTMwNDY4ODY0.DoxqQA.5yev1BulYMNRI_7_uAjaEyyMWo8"


async def my_background_task():
    await client.wait_until_ready()
    msg = 'Test'
    channel = discord.Object(id='494322306122907649')
    # for i in range(0,1):
    # counter += 1
    await client.send_message(channel, msg)
    client.logout()
    # await asyncio.sleep(60) # task runs every 60 seconds


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(my_background_task())
client.run(token)
