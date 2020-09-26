import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time


client = discord.Client()

owner = ['724769557759393837']
@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["원라인 많이 이용해주세요", "원라인 인증" , "!인증" , str(user) + "분이 인증을 완료 하셨습니다.", str(server) + "님이 인증을 완료 못 하셨어요"]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)
            
@client.event
async def on_message(message):
  if message.content == "!인증":
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = "Captcha.png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        embed = discord.Embed(title="당신의 요청으로 인증코드가 만들어졌습니다.", description = message.author.mention + ", 위에 있는 인증코드를 20초내에 입력해주세요.", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        embed.set_footer(text="원라인에 오신것을 진심으로 환영합니다.", icon_url="https://media.discordapp.net/attachments/735766686090788874/759404838404227072/e6f11eee6427bcbd.png")
        await message.channel.send(embed=embed)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증시간 ( 20초 ) 를 초과했어요.", timestamp=message.created_at,
            colour=discord.Colour.orange()
    )
            embed.set_footer(text="아쉬워요 하지만 다시 할 수 있어요", icon_url="https://media.discordapp.net/attachments/735766686090788874/759404838404227072/e6f11eee6427bcbd.png")
            await message.channel.send(embed=embed)

        if msg.content == a:
            embed = discord.Embed(title="성공!", description = message.author.mention + ", __**Captcha**__ 인증코드를 정확히 입력하여 USER 권한이 지급되었어요! 좋은 시간 되세요 :) 규칙은 확인하셨지요?", timestamp=message.created_at,
            colour=discord.Colour.green()
    )
            embed.set_footer(text="즐거운 하루 되시고 상대방에게 말을 조심하세요. 규칙을 확인하세요 ;)", icon_url="https://media.discordapp.net/attachments/735766686090788874/759404838404227072/e6f11eee6427bcbd.png")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.author.guild.roles, name='🐥ㅣ시민')
            await message.author.add_roles(role)
        
        else:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증코드가 올바르지 않아요! 다시 시도해봐요.", timestamp=message.created_at,
            colour=discord.Colour.red()
    )
            embed.set_footer(text="아쉬워요 하지만 다시 가능하답니다 ;)", icon_url="https://media.discordapp.net/attachments/735766686090788874/759404838404227072/e6f11eee6427bcbd.png")
            await message.channel.send(embed=embed)
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
