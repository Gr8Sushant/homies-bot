# bot.py
import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} is now connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Vsdk welcome to our server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    res = [
         'Nice!!', 'VSDK', 'Hot funeral selfies', 'I slay it, Queen'
    ]

    if message.content == '69':
        response = random.choice(res)
        await message.channel.send(response)

client.run(TOKEN)


