import discord
import random
import os
import tweepy
import json
from discord.ext import commands


privateData = json.loads(open('privateData.json').read())
randomBotData = json.loads(open('randomBotData.json').read())

auth = tweepy.OAuthHandler(privateData['Twitter_Consumer_Key'], privateData['Twitter_Consumer_Secret'])
auth.set_access_token(privateData['Twitter_Access_Key'], privateData['Twitter_Access_Secret'])
api = tweepy.API(auth)

client = commands.Bot(command_prefix = '$')

@client.event

@client.event
async def on_member_join(member):
    print(f'{member} has joined Fumpledump Enterprise!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left Fumpledump Enterprise!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NjYyMTA1Mjc3MzAyMDQ2Nzcw.XhGjyQ.rRcMJvjXnwIAs4FV5L6MBBxkvNg')
