# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    optimus_quotes = [
        ('In any war, there are calms between storms. There will be days when we lose faith.'
         ' Days when our allies turn against us...but the day will never come that we forsake'
         ' this planet and its people.'),
        'Freedom is the right of all sentient beings.',
        'Fate rarely calls upon us at a moment of our choosing.',
        'I am Optimus Prime, and I send this message to the universe: We are here. We are home.',
        (
        'Do not lament my absence, for in my spark, I know that this is not the end,'
        ' but merely a new beginning. Simply put, another transformation.'
        ),
        'TRANSFORM AND ROLL OUT',
        
    ]
    
    decepticon_mentioned = [
        'Let them come',
        'OUR WORLDS ARE IN DANGER',
        'he played me like a piano!',
        (
        'TO SAVE THEM AND THE GALAXY WE MUST FIND THE FOUR CYBER PLANET KEYS'
        ' BEFORE THE DECEPTICONS CAN USE THEM FOR EVIL'
        ),
    ]

    keywords = ["optimus", "prime", "autobot", "autobots"]
    decep_keywords = ['decepticon', 'decepticons', 'megatron']

    if any(decep_keyword in message.content.lower() for decep_keyword in decep_keywords):
        response = random.choice(decepticon_mentioned)
        await message.channel.send(response)
    elif any(keyword in message.content.lower() for keyword in keywords):
        response = random.choice(optimus_quotes)
        await message.channel.send(response)


    

client.run(TOKEN)