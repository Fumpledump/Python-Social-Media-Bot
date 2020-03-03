import discord
import random
import os
import json
from discord.ext import commands
randomBotData = json.loads(open('randomBotData.json').read())

class CommandList(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(self.client.user.name)
        print(self.client.user.id)
        print('~~~~~~~~~~~~~~~~~~')


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Here is your Ping : {round(self.client.latency * 1000)}ms')

    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, ctx, *, question='None was provided...'):
        responses = randomBotData['8ball_responses']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
    client.add_cog(CommandList(client))
