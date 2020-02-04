import discord
import random
import os
from discord.ext import commands

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
        responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."
                ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
    client.add_cog(CommandList(client))
