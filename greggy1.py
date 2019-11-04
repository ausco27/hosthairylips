import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import string
import os
import youtube_dl
from discord import Game
from discord.utils import get
from discord.ext import commands
from ctypes.util import find_library
from discord import opus

Client = discord.Client()
client = commands.Bot(command_prefix = '!')
client.remove_command('help')

players = {}

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hi':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/622570415138668566/37531288_10214845934209236_5894293850083557376_n.jpg')
        await client.send_message(message.channel,"hello :slight_smile: {0.author.mention}".format(message), embed=em)
    if message.content == 'hello':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/622569776094380032/10931170_10205885682568545_733491445515429267_n.jpg')
        await client.send_message(message.channel,"hey baby :wink: {0.author.mention}".format(message), embed=em)
    if message.content == 'hey':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/622569776094380032/10931170_10205885682568545_733491445515429267_n.jpg')
        await client.send_message(message.channel,"hey baby :wink: {0.author.mention}".format(message), embed=em)
    if message.content == 'Hey':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/622569776094380032/10931170_10205885682568545_733491445515429267_n.jpg')
        await client.send_message(message.channel,"hey baby :wink: {0.author.mention}".format(message), embed=em)
    if message.content == 'Hi':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/622567851290656768/885093_10200461614450232_455002775_o.jpg')
        await client.send_message(message.channel,"hey sexy :wink: {0.author.mention}".format(message), embed=em)
    if message.content == 'Hello':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/622569776094380032/10931170_10205885682568545_733491445515429267_n.jpg')
        await client.send_message(message.channel,"hey sexy :wink: {0.author.mention}".format(message), embed=em)
    if message.content == 'hairylips_kid1':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/620875753403187220/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'hairylips_kid2':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/620876412559294475/Screenshot_2019-08-19-01-16-00.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'hairylips_kid3':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/619793166610202634/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'hairylips_kid4':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/619789281900101642/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'hairylipds_kid5':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/619789562981515265/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'allyboob':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/617558283783372801/Screenshot_2019-08-31-21-52-30.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'allyboob2':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/617558285158973469/Screenshot_2019-08-31-21-46-49.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'allyboob3':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/617558283783372800/Screenshot_2019-08-31-21-45-38.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'allyforehead':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/613206125818675210/Screenshot_2019-08-19-21-22-10.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'allybelly':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/612137550710308865/allie3.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'allychest':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/612139731085557767/allie5.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'hairylips_dick':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/609270234175766543/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'hairylips_dick2':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/586810989840826368/608882635711971338/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'hairylips_dick3':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609215081242427448/609216098830778376/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'knight':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609596296885436424/621219800093556736/Capture.PNG')
        await client.send_message(message.channel, embed=em)
    if message.content == 'blood':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/621244038942818315/621542061237075978/image0.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'laura':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609680315220230144/627385197142474822/unknown.png')
        await client.send_message(message.channel, embed=em)

    if message.author == client.user:
        return
    if message.content.startswith('.iamgreggy'):
        role = get(message.server.roles, name='follower')
        await client.add_roles(message.author,role)

    if message.content.startswith('hairylips_fansign'):
        embed = discord.Embed()
        zack1 = "https://cdn.discordapp.com/attachments/609215081242427448/609215336624947210/unknown.png"
        zack2 = "https://cdn.discordapp.com/attachments/609215081242427448/609215428551770133/unknown.png"
        zack3 = "https://cdn.discordapp.com/attachments/609215081242427448/609216408240521216/ilovehairylips.png"
        zack4 = "https://cdn.discordapp.com/attachments/609215081242427448/609216462212825098/hairylips.jpg"
        zack5 = "https://cdn.discordapp.com/attachments/609215081242427448/609252194688040988/JPEG_20190809_000847.jpg"
        zack6 = "https://cdn.discordapp.com/attachments/609215081242427448/609283600382296090/unknown.png"
        zack7 = "https://cdn.discordapp.com/attachments/609215081242427448/609287672720130052/unknown.png"
        zack8 = "https://cdn.discordapp.com/attachments/609215081242427448/609288415267127339/unknown.png"
        zack9 = "https://cdn.discordapp.com/attachments/609215081242427448/609289681695277057/iamhairylips2.jpg"
        zack10 = "https://cdn.discordapp.com/attachments/609215081242427448/609685277178593290/unknown.png"
        zack11 = "https://cdn.discordapp.com/attachments/609215081242427448/609691991458185217/unknown.png"
        zack12 = "https://cdn.discordapp.com/attachments/609215081242427448/609692085607464969/unknown.png"
        zack13 = "https://cdn.discordapp.com/attachments/609215081242427448/610316565208104962/unknown.png"
        zack14 = "https://cdn.discordapp.com/attachments/609215081242427448/610682465480081408/unknown.png"
        zack15 = "https://cdn.discordapp.com/attachments/609215081242427448/612133744006004736/allie.jpg"
        zack16 = "https://cdn.discordapp.com/attachments/609215081242427448/612134472195768361/allie2.jpg"
        zack17 = "https://cdn.discordapp.com/attachments/609215081242427448/612137550710308865/allie3.jpg"
        zack18 = "https://cdn.discordapp.com/attachments/609215081242427448/612139731085557767/allie5.jpg"
        zack19 = "https://cdn.discordapp.com/attachments/609215081242427448/612506292862582794/WIN_20190817_22_34_50_Pro.jpg"
        zack20 = "https://cdn.discordapp.com/attachments/609215081242427448/612818974152851478/unknown.png"
        zack21 = "https://cdn.discordapp.com/attachments/609215081242427448/613206125818675210/Screenshot_2019-08-19-21-22-10.png"
        zack22 = "https://cdn.discordapp.com/attachments/609215081242427448/613224294205489152/unknown.png"
        zack23 = "https://cdn.discordapp.com/attachments/609215081242427448/619044525712736277/hairylipsblack.jpg"
        zack24 = "https://cdn.discordapp.com/attachments/609215081242427448/619789562981515265/unknown.png"
        zack25 = "https://cdn.discordapp.com/attachments/609215081242427448/619789767390920704/unknown.png"
        zack26 = "https://cdn.discordapp.com/attachments/609215081242427448/619793166610202634/unknown.png"
        zack27 = "https://cdn.discordapp.com/attachments/609215081242427448/619796998203375666/unknown.png"
        zack28 = "https://cdn.discordapp.com/attachments/609215081242427448/619797056533430302/unknown.png"
        zack29 = "https://cdn.discordapp.com/attachments/609215081242427448/619797156462592030/unknown.png"
        zack30 = "https://cdn.discordapp.com/attachments/609215081242427448/619797994472210432/unknown.png"
        zack31 = "https://cdn.discordapp.com/attachments/609215081242427448/619799056264462336/unknown.png"
        zack32 = "https://cdn.discordapp.com/attachments/609215081242427448/619799777265319936/unknown.png"
        zack33 = "https://cdn.discordapp.com/attachments/609215081242427448/619799998200283147/unknown.png"
        zack34 = "https://cdn.discordapp.com/attachments/609215081242427448/619819813119983616/unknown.png"
        zack35 = "https://cdn.discordapp.com/attachments/609215081242427448/619819859752124437/unknown.png"
        zack36 = "https://cdn.discordapp.com/attachments/609215081242427448/619822084461428746/unknown.png"
        zack37 = "https://cdn.discordapp.com/attachments/609215081242427448/619939055471427585/Screenshot_2019-09-03-23-41-11.png"
        zack38 = "https://cdn.discordapp.com/attachments/609215081242427448/620875753403187220/unknown.png"
        zack39 = "https://cdn.discordapp.com/attachments/609215081242427448/620876412559294475/Screenshot_2019-08-19-01-16-00.png"
        embed.set_image(url = random.choice([zack1, zack2, zack3, zack4, zack5, zack6, zack7, zack8, zack9, zack10, zack11, zack12, zack13, zack14, zack15, zack16, zack17, zack18, zack19, zack20, zack21, zack22, zack23, zack24, zack25, zack26, zack27, zack28, zack29, zack30, zack31, zack32, zack33, zack34, zack35, zack36, zack37, zack38, zack39 ]))
        await client.send_message(message.channel, embed=embed) 
    if message.content.startswith('pedo#1'):
        embed = discord.Embed()
        ped1 = "https://cdn.discordapp.com/attachments/609215081242427448/609685277178593290/unknown.png"
        ped2 = "https://cdn.discordapp.com/attachments/609215081242427448/609689290602971146/unknown.png"
        ped3 = "https://cdn.discordapp.com/attachments/609215081242427448/609691991458185217/unknown.png"
        ped4 = "https://cdn.discordapp.com/attachments/609215081242427448/609692085607464969/unknown.png"
        embed.set_image(url = random.choice([ped1, ped2, ped3, ped4]))
        await client.send_message(message.channel, embed=embed) 
    if message.content.startswith('pedo#2'):
        embed = discord.Embed()
        pedo1 = "https://cdn.discordapp.com/attachments/609680315220230144/620858923737677834/unknown.png"
        pedo2 = "https://cdn.discordapp.com/attachments/609680315220230144/620858641662214145/unknown.png"
        pedo3 = "https://cdn.discordapp.com/attachments/609596296885436424/620911647547981855/Capturefasdfsdf.PNG"
        pedo4 = "https://cdn.discordapp.com/attachments/609596296885436424/620859004461252618/unknown.png"
        pedo5 = "https://cdn.discordapp.com/attachments/609596296885436424/620859186888179712/unknown.png"
        embed.set_image(url = random.choice([pedo1, pedo2, pedo3, pedo4, pedo5]))
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith('pedo#3'):
        embed = discord.Embed()
        pedo1 = "https://cdn.discordapp.com/attachments/522488319511101456/627444442307231744/unknown.png"
        embed.set_image(url = random.choice([pedo1]))
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith('moistnigerian'):
        embed = discord.Embed()
        moist1 = "https://cdn.discordapp.com/attachments/609596123870527498/621216184863555584/5e20ea32eab065562b4e3b99e9211ce8.png"
        moist2 = "https://cdn.discordapp.com/attachments/609596123870527498/621216192996311050/unknown3.png"
        moist3 = "https://cdn.discordapp.com/attachments/609596123870527498/621216202835886080/unknown.png"
        moist4 = "https://cdn.discordapp.com/attachments/609596123870527498/621216205952253952/Screenshot_1.png"
        moist5 = "https://cdn.discordapp.com/attachments/609596123870527498/621216212470464523/unknown_4.png"
        moist6 = "https://cdn.discordapp.com/attachments/609596123870527498/621216229482561536/image0_3.jpg"
        moist7 = "https://cdn.discordapp.com/attachments/609596123870527498/621216230841384960/unknown_2.png"
        moist8 = "https://cdn.discordapp.com/attachments/609596123870527498/621216234309943306/Screenshot_2.png"
        moist9 = "https://cdn.discordapp.com/attachments/609596123870527498/621216235891458059/unknown_1.png"
        moist10 = "https://cdn.discordapp.com/attachments/609596123870527498/621216242438766592/20190905_201525.jpg"
        embed.set_image(url = random.choice([moist1, moist2, moist3, moist4, moist5, moist6, moist7, moist8, moist9, moist10]))
        await client.send_message(message.channel, embed=embed)
    
    if 'kiss' in message.content:
        em = discord.Embed(description='muah 😘')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/621122399894634496/unknown.png')
        await client.send_message(message.channel, embed=em)
    
    if 'offer food' in message.content:
        em = discord.Embed(description='u want some??')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/621126107776679936/31478685_10214276224166841_3800069196713295872_n.jpg')
        await client.send_message(message.channel, embed=em)

    if 'good morning' in message.content:
        em = discord.Embed(description='wakey wakey sunshine')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/622566995568754718/44902220_10215576804120527_3234849426090491904_n.jpg')
        await client.send_message(message.channel, embed=em)
        
    if 'good night' in message.content:
        em = discord.Embed(description='good night')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/622567179447042068/1558513_10202833534906761_1793325379_n.jpg')
        await client.send_message(message.channel, embed=em)
    
    if 'avery' in message.content:
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609680315220230144/638644383121539072/image0.jpg')
        await client.send_message(message.channel, embed=em)

    if 'dweeb' in message.content:
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/609680315220230144/638628135889534976/image0.png')
        await client.send_message(message.channel, embed=em)


    if "<@621084932361420813>" in message.content:
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/622578415416901643/11257786_10205850274163357_1852257735542021520_n.jpg')
        await client.send_message(message.channel, embed=em)
    if message.author.id == "asd":
        emoji1 = get(client.get_all_emojis(), name='mecute')
        emoji2 = get(client.get_all_emojis(), name='mecute2')
        emoji3 = get(client.get_all_emojis(), name='mecute3')
        await client.add_reaction(message, emoji=emoji1)
        await client.add_reaction(message, emoji=emoji2)
        await client.add_reaction(message, emoji=emoji3)
    if message.author.id == "asd":
        await client.add_reaction(message, emoji='🇩')
        await client.add_reaction(message, emoji='🇪')
        await client.add_reaction(message, emoji='🇾')
        await client.add_reaction(message, emoji='🇲')
    if message.author.id == "asd":
      emoji4 = get(client.get_all_emojis(), name='kids')
      await client.add_reaction(message, '🇮')
      await client.add_reaction(message, '❤')
      await client.add_reaction(message, emoji=emoji4)

    if message.channel.is_private == True: # This is a direct message: Private Message
        print("Private", message.author, message.content) 

 ##   if message.author.id == '201546529973075968':
 ##       em = discord.Embed(description='')
 ##       await client.send_message(discord.Object(id='522488319511101456'),'message')

    await client.process_commands(message)

@client.event  
async def on_raw_reaction_add(payload):
    print("Hello.") 


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 640827565300383764: 
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'greggy':
            role = discord.utils.get(guild.roles, name='slave')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_remove(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")

@client.command(pass_context=True)
async def info(ctx, member: discord.Member = None):
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=member.colour, timestamp=ctx.message.timestamp)
    embed.set_author(name=member)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Nickname:", value=member.display_name)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)
    await client.send_message(ctx.message.channel,embed=embed)

@client.command(pass_context = True)
async def serverinfo(ctx):
    
    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles)
    channelz = len(server.channels)
    time = str(server.created_at); time = time.split(' '); time= time[0]

    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', colour = 0xFFFF)
    join.set_thumbnail(url = server.icon_url)
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id)
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count))
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz))
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles)
    join.set_footer(text ='Created: %s'%time)

    return await client.say(embed = join)

@client.command(pass_context=True)
async def avatar(con,user:discord.Member):
    emb=discord.Embed(title=user.name + ' aka my girlfriend')
    emb.set_image(url=user.avatar_url)
    await client.send_message(con.message.channel,embed=emb)

@client.command(pass_context=True)
async def ping(ctx):
   	channel = ctx.message.channel
   	t1 = time.perf_counter()
   	await client.send_typing(channel)
   	t2 = time.perf_counter()
   	embed=discord.Embed(title="Pong!", description='It took {}ms.'.format(round((t2-t1)*1000)), color=0xffffff)
   	await client.say(embed=embed)
    
@client.command(pass_context=True)
async def quote(ctx,member:discord.Member, *, content):
    user_msg=ctx.message
    embed = discord.Embed(description = content, colour=member.colour, timestamp=ctx.message.timestamp)
    embed.set_author(name=member.name , icon_url=member.avatar_url)
    await asyncio.sleep(1)
    await client.delete_message(user_msg)
    await client.send_message(ctx.message.channel,embed=embed)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="naked girls", type = 3))
    print('Bot online.')


@client.command(pass_context=True)
async def say(ctx, *msg):
    if ctx.message.author.id == "201546529973075968":
        user_msg=ctx.message
        await client.say("{}".format(" ".join(msg)))
        await asyncio.sleep(.1)
        await client.delete_message(user_msg)
    else:
        await client.send_message(ctx.message.channel, "only my boss can tell me wat to say")

@client.command(pass_context=True)
async def members(ctx):
    embed = discord.Embed(title="Member Count", description=str(len(ctx.message.server.members)), color=0x149900)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def online(con):
    amt = 0
    for i in con.message.server.members:
        if i.status != discord.Status.offline:
            amt += 1
    await client.send_message(con.message.channel, "**Currently `{}` Members Online In `{}`**".format(amt,con.message.server.name))

@client.command(pass_context=True)
async def offline(con):
    amt = 0
    for i in con.message.server.members:
        if i.status == discord.Status.offline:
            amt += 1
    await client.send_message(con.message.channel, "**Currently `{}` Members Offline In `{}`**".format(amt,con.message.server.name))

@client.command(pass_context=True)
async def afks(con):
    amt=0
    for i in con.message.server.members:
        if i.is_afk == True:
            amt+=1
    await client.send_message(con.message.channel,"**Currently `{}` AFK Members In `{}`**".format(amt,con.message.server.name))

@client.command(pass_context=True)
async def greggy(ctx, *, message):
    channel = client.get_channel("609596296885436424")
    await client.send_message(channel, message)

@client.command(pass_context=True)
async def creep(ctx, member: discord.Member, *, message):
    await client.send_message(member, message)

@client.command(pass_context=True)
async def sendlove(ctx, member: discord.Member):
    await client.send_message(member, '💕💕💕')
    print ("love sent")

@client.command(pass_context=True)
async def unban(con,user:int):
    if con.message.author.id == "201546529973075968":
        try:
            who=await client.get_user_info(user)
            await client.unban(con.message.server,who)
            print ("member unbanned")
        except:
            await client.say("Something went wrong")
    else:
        await client.send_message(con.message.channel, "u are not cute enough")

@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '201546529973075968':
        role = discord.utils.get(member.server.roles, name='muted')
        await client.add_roles(member, role)
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/627326563993780224/unknown.png')
        fmt = 'you have been silenced by me!! *{0.mention}*'
        channel = member.server.get_channel("609596296885436424")
        await client.send_message(channel, fmt.format(member, member.server), embed=em)

     else:
        em=discord.Embed(title="nope!!!", description="true greggys fans only", color=0xff00f6)
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/627330121925132288/600343_10200433094097241_773766898_n.jpg')
        await client.say(embed=em)

@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '201546529973075968':
        role = discord.utils.get(member.server.roles, name='muted')
        await client.remove_roles(member, role)
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/627330824571977728/47230852_10215845139948755_8474825117665329152_n.jpg')
        fmt = 'you may now chat again *{0.mention}*'
        channel = member.server.get_channel("609596296885436424")
        await client.send_message(channel, fmt.format(member, member.server), embed=em)

     else:
        em=discord.Embed(title="nope!!!", description="true greggys fans only", color=0xff00f6)
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/627330121925132288/600343_10200433094097241_773766898_n.jpg')
        await client.say(embed=em)

@client.event
async def on_member_remove(member):
    em = discord.Embed(description='✌')
    em.set_image(url='https://cdn.discordapp.com/attachments/621086945510031360/627323136357957633/unknown.png')
    fmt = '{0.mention} *{0}* bye bye ugly ass'
    channel = member.server.get_channel("609596296885436424")
    await client.send_message(channel, fmt.format(member, member.server), embed=em)

@client.event
async def on_member_join(member):
    em = discord.Embed(description='😘 read the rules to get access to the whole server')
    em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/621203042121023488/12289770_10207180857547110_6170230403992296839_n.jpg')
    fmt = 'hey {0.mention} wanna be my girlfriend?? 🤤🤤'
    channel = member.server.get_channel("609596296885436424")
    await client.send_message(channel, fmt.format(member, member.server), embed=em)

extensions = ['example', 'penis', 'Example']

@client.command()
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))

@client.command()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded. [{}]'.format(extension, error))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

client.run(("NjIxMDg0OTMyMzYxNDIwODEz.XXgPzw.dEubs2UNyTMaNTne393tlLi2HbQ"))