import discord
from discord.ext import commands
import asyncio
import random
from discord.utils import *

yakumo = commands.Bot(command_prefix='y.')

@yakumo.event
async def on_ready():
    print(yakumo.user.name)

@yakumo.command(pass_context=True)
async def dice(con,min1=1,max1=6):
    await yakumo.say("**{}**".format(random.randint(min1,max1)))


@yakumo.command(pass_context=True)
async def pin(con,*,msg):
    await yakumo.pin_message(msg)

@yakumo.command(pass_context=True)
async def react(con,msg_id,emoji):
    emote= get(yakumo.get_all_emojis(),name=emoji)
    msg= await yakumo.get_message(con.message.channel,msg_id)
    await yakumo.add_reaction(msg,emoji=emote)

yakumo.run('NTE5MjM3MzEyMjk5Nzk0NDMy.DuckcA.THLgG7x4Gp2GBxQEJqbjd4xQVAM')
