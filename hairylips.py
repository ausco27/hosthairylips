import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import string
from discord import Game
from discord.utils import get
from discord.ext import commands
from ctypes.util import find_library
from discord import opus

Client = discord.Client()
client = commands.Bot(command_prefix = 'hairy.')
client.remove_command('help')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hi'):
        await client.send_message(message.channel,"hey sexy :wink: {0.author.mention}".format(message))
    if message.content.startswith('hello'):
        await client.send_message(message.channel,"hey baby :wink: {0.author.mention}".format(message))
    if message.content.startswith('Hi'):
        await client.send_message(message.channel,"hey sexy :wink: {0.author.mention}".format(message))
    if message.content.startswith('Hello'):
        await client.send_message(message.channel,"hey sexy :wink: {0.author.mention}".format(message))
    if message.content.startswith('hey guys'):
        await client.send_message(message.channel,"hey girl :wink: {0.author.mention}".format(message))
    if message.content.startswith('Hey guys'):
        await client.send_message(message.channel,"hey girl :wink: {0.author.mention}".format(message))
    if message.content == 'hoy':
        await client.send_message(message.channel,'hoyy')
    if message.content == 'Hoy':
        await client.send_message(message.channel,'hoyy')
    if message.content == 'good morning':
        await client.send_message(message.channel,'good morning sunshine! <3')
    if message.content == 'Goodmorning':
        await client.send_message(message.channel,'good morning sunshine! <3')
    if message.content == 'morning':
        await client.send_message(message.channel,'morning babe')
    if message.content == 'Morning':
        await client.send_message(message.channel,'good morning babe')
    if message.content == 'goodmorning':
        await client.send_message(message.channel,'good morning baby')
    if message.content == ';gal':
        await client.send_message(message.channel,'hey gal...')
    if message.content == ';dragon':
        await client.send_message(message.channel,'is gay')
    if message.content == ';lawrence':
        await client.send_message(message.channel,'sucks dick')
    if message.content == 'peppermint':
        await client.send_message(message.channel,'can i have a peppermint? you can have a peppermint! bleh! hay! ahh! i dont like the peppermint! you dont like the peppermint! its too spiceee!')
    if message.content == 'lawrence':
        await client.send_message(message.channel,'is a big gay')
    if message.content == ';mikey':
        await client.send_message(message.channel,'is my bitch')
    if message.content == ';banana':
        await client.send_message(message.channel,'is my ex-girlfriend')
    if message.content == ';gay':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519252854951903262/makeup.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';sleepynana':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519264497408409610/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';poge':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519265398487777280/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';bakla':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/509927893741076480/517671960583602239/FB_IMG_1543491997341.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == ';jayzee':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519270198059204628/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == 'jamason diss':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/520060319415009280/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';maotsi':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519270579346341889/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';deym':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/519931040723238913/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';ice':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519253014536519683/ice3.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == ';jemsbond':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519624883999866921/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';cuteboy':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/509927893741076480/517328497455267840/image0.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == ';umar':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519624992917291009/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';nana':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519253176814403605/banana4.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';shootyou':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/261382678111191040/519413085816094722/umar6.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == ';pogi':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519268272063905792/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';maxime':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519253702142459919/max.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == ';handsome':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519315393882357773/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';ilong':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519542331091976194/nose.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == ';lolomo':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519542773444247555/lol1.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == ';gf':
        em = discord.Embed(description='this is my ex-gf')
        em.set_image(url='https://cdn.discordapp.com/attachments/397727233688600577/519549246706548736/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';autumn':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/509927893741076480/519661416693628949/image0.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == ';ryan':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/501820654606221312/519622744258641931/F7ia3Fy.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';allie':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/501447875742400513/501448827086045196/image1.PNG')
        await client.send_message(message.channel, embed=em)
    if message.content == ';babe':
        em = discord.Embed(description='this is my babe')
        em.set_image(url='https://cdn.discordapp.com/attachments/509927893741076480/521012572070084608/IMG_20181209_011655.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == ';2ndgf':
        em = discord.Embed(description='this is my other girlfriend')
        em.set_image(url='https://cdn.discordapp.com/avatars/488359947919294475/8a37087b76481cdf8d21bd32895003c5.png?size=256')
        await client.send_message(message.channel, embed=em)
    if message.content == ';mygf':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/avatars/313481759029460992/0a99ca0d4f509f0daffb06aac79ded9b.png?size=256')
        await client.send_message(message.channel, embed=em)
    if message.content == ';gallovesme':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/521875304571207700/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';jopaylovesme':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/521875692821020675/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';tiffalovesme':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/521875692821020675/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';mikulovesme':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/521875901793697792/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';bananalovesme':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/521876045041762334/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';myllzlovesme':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/521886666550411285/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';jeplovesme':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/521887092561936387/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';autumnlovesme':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/522206051312074776/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content == ';facetime':
        em = discord.Embed(description='facetiming with my boyfriend')
        em.set_image(url='https://cdn.discordapp.com/attachments/511734629372526625/522309548787236876/unknown.png')
    if message.content == ';graylovesme':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/522488319511101456/523186063334703104/unknown.png')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('dechy diss'):
        randomlist = ["Sayin my makeup looks like trash but who are you?", "Hiding behind a profile no pictures to view", "Acting like im ugly what an insult i think i need a tissue", "You silly you dont know the bars im bout to chew through", "Ha you rapped once and said that you were better than me", "thats funny cuz u sounded like a french preteen", "you were stumbling through your words a social disgracee", "If you think you are better thats a joke and not reality", "To be honest when i met you i thought u were a dude", "Yo voice is annoying and your mouth should just stay glued", "Sounding like a kid all moody and rude", "Just shut yo mouth stop making everyone feel devalued", "Ima ask you to just sit back missy", "Your “roasts” are some of the most basic things I've ever heard", "It's like you want attention", "Saying the same stuff that made me mad over and over again", "Well now people will be playing this track over and over again", "Do you really think I gave a __", "I had had u on ur knees apologising dumbstruck", "I was getting a show for my buck", "U thought I cried!? Hahaha not today Donald Duck"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('rosie diss'):
        randomlist = ["why are you crouching in front of grass you look like a hungry cow", "@Rose#7420 did you sleep well, you didnt snore?", "nice @Rose#7420 we really are interresed in your sleeping schedule", "Rose been so long how are you ? you still snore? still depresed? still look like a pig?", "Rose dont get pissed off like destroyer", "I beat you in real life, csgo, and fortnite", "I can beat you up so easily, ur fat so ur slow", "Rose you look like a pig so shot the fok up", "Maxime and me make better role plays than Rose", "gonna get mickeyd aigan", "you had to ask for the compliment and then he compared you to shit @Rose", "be carefull that Chris dosent see your youtube channel @Rose#7420", "cool @Rose#7420 so interesting", "piggy piggy where you at", "rose where the fuck s ur sis swan need to talk to her", "l0l rose lost her virginity at church camp"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('feminine'):
        embed = discord.Embed()
        zack1 = "https://cdn.discordapp.com/attachments/486494894576238592/514047711893520405/IMG_20181119_195831_158.jpg"
        zack2 = "https://cdn.discordapp.com/attachments/486494894576238592/510280544521551883/45652649_280670942559144_5638239912919564288_n.jpg"
        zack3 = "https://i.imgur.com/LNgU9Lk.png"
        zack4 = "https://cdn.discordapp.com/attachments/486494894576238592/507733436492939274/45228783_1456940857773249_9080876523895914496_n.png"
        zack5 = "https://cdn.discordapp.com/attachments/486494894576238592/507470791030603786/19884133_1120031398130865_1458742456387798836_n.png"
        zack6 = "https://i.imgur.com/iAU49SY.png"
        embed.set_image(url = random.choice([zack1, zack2, zack3, zack4, zack5, zack6]))
        await client.send_message(message.channel, embed=embed)
    if "<@519237312299794432>" in message.content:
        await client.send_message(message.channel,'yes baby')
    if message.author.id == "201546529973075968":
        emoji1 = get(client.get_all_emojis(), name='mecute')
        emoji2 = get(client.get_all_emojis(), name='mecute2')
        emoji3 = get(client.get_all_emojis(), name='mecute3')
        await client.add_reaction(message, emoji=emoji1)
        await client.add_reaction(message, emoji=emoji2)
        await client.add_reaction(message, emoji=emoji3)
    if message.author.id == "20asdasdasd":
        await client.add_reaction(message, emoji='🇩')
        await client.add_reaction(message, emoji='🇪')
        await client.add_reaction(message, emoji='🇾')
        await client.add_reaction(message, emoji='🇲')
    if message.author.id == "452646134343794":
      emoji4 = get(client.get_all_emojis(), name='mecute')
      await client.add_reaction(message, '🇮')
      await client.add_reaction(message, '❤')
      await client.add_reaction(message, emoji=emoji4)

    if message.channel.is_private == True: # This is a direct message: Private Message
        print("Private", message.author, message.content) 

 ##   if message.author.id == '201546529973075968':
 ##       em = discord.Embed(description='')
 ##       await client.send_message(discord.Object(id='522488319511101456'),'message')

    await client.process_commands(message)

@client.command(pass_context=True)
async def stalk(ctx, member: discord.Member = None):
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

async def timer_bg(con, time):
    tc=[]
    timer = time
    ct = con.message.channel.id
    if ct in tc:
        await client.send_message(con.message.channel, "Please wait for the current timer to complete.")
    elif ct not in tc:
        msg = await client.send_message(con.message.channel, time)
        tc.append(con.message.channel.id)
        for i in range(time):
            await asyncio.sleep(1)
            timer -= 1
            await client.edit_message(msg, new_content=timer)
        num = tc.index(ct)
        del tc[num]
        await client.send_message(con.message.channel, "boom".format(time))
        
@client.command(pass_context=True)
async def timer(con, time:int=10):
    client.loop.create_task(timer_bg(con, time)) 

@client.command(pass_context=True)     
async def say(ctx, *msg):
    user_msg=ctx.message
    await client.say("{}".format(" ".join(msg)))
    await asyncio.sleep(.1)
    await client.delete_message(user_msg)

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
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name='Help')
    embed.add_field(name='hairy.join', value='hairy lips cuddles with you', inline=False)
    embed.add_field(name='hairy.play <song name/url>', value='hairy lips sings you the song', inline=False)
    embed.add_field(name='hairy.pause', value='pauses the music', inline=False)
    embed.add_field(name='hairy.resume', value='resumes the music', inline=False)
    embed.add_field(name='hairy.stop', value='hairy lips stops singing', inline=False)
    embed.add_field(name='hairy.leave', value='hairy lips leaves but still loves you', inline=False)
    await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context=True)
async def broadcast(ctx, *, message):
    channel = client.get_channel("521894876925919243")
    await client.send_message(channel, message)

@client.command(pass_context=True)
async def sendlove(ctx, member: discord.Member):
    await client.send_message(member, '💕💕💕')

@client.command(pass_context=True)
async def delete(con,ide:str):
    msg=await client.get_message(con.message.channel,ide)
    await client.delete_message(msg)

@client.command(pass_context=True)
async def unban(con,user:int):
    try:
        who=await client.get_user_info(user)
        await client.unban(con.message.server,who)
    except:
        await client.say("Something went wrong")
##author = ctx.message.author
##@client.event
##async def on_message(msg):
##    if msg.channel.is_private == True: # This is a direct message: Private Message
##        print("Private")
##    if msg.channel.is_private == False: #Mesage is from a server, not in Direct Message
##        print("Public")
##async def on_member_join(member):
##    print('Recognised that a member called ' + member.name + ' joined')
##    await client.send_message(member, 'hey do you wanna be my girlfriend?? add me: hairy lips#7774')
##    print('Sent message to ' + member.name)

client.run('NTE5MjM3MzEyMjk5Nzk0NDMy.DuckcA.THLgG7x4Gp2GBxQEJqbjd4xQVAM')