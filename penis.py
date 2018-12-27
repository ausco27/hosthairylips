import discord
from discord.ext import commands
import random

class Penis:
    """Penis related commands."""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def penis(self, user : discord.Member):
        """Detects user's penis length
        This is 100% accurate."""
        random.seed(user.id)
        p = "8" + "="*random.randint(0, 30) + "D"
        await self.client.say("Size: " + p)

    @commands.command(pass_context=True)
    async def rate(self, ctx, *, user:discord.Member):
        """Rate something."""
        if user.id == ctx.message.server.me.id:
            await self.client.say("I would rate myself a 10/10.")
            return
        elif user.id == 201546529973075968:
            await self.client.say("I would rate my owner a 10/10.")
            return
        await self.client.say("I would rate {} a {}/10.".format(user.mention, random.randint(0, 10)))


def setup(client):
    client.add_cog(Penis(client))
