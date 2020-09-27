import discord
from captcha.image import ImageCaptcha
import time
import os
import captcha
import random

client = discord.Client()

@client.event
async def on_ready():
    print("인증 봇이 정상적으로 실행되었습니다.")
    game = discord.Game('원라인 인증 하는중 ! ')
    await client.change_presence(status=discord.Status.online, activity=game)

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
        embed = discord.Embed(title="인증코드가 만들어졌어요.", description = message.author.mention + ", 위에 있는 인증코드를 10초내에 입력해주세요.", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        embed.set_footer(text="10초 후에 만료되요 ! ", icon_url="https://media.discordapp.net/attachments/735766686090788874/759404838404227072/e6f11eee6427bcbd.png")
        await message.channel.send(embed=embed)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증시간 ( 10초 ) 를 초과했어요.", timestamp=message.created_at,
            colour=discord.Colour.orange()
    )
            embed.set_footer(text="원라인 인증 도우미", icon_url="https://media.discordapp.net/attachments/735766686090788874/759404838404227072/e6f11eee6427bcbd.png")
            await message.channel.send(embed=embed)

        if msg.content == a:
            embed = discord.Embed(title="성공!", description = message.author.mention + ", __**Captcha**__ 인증코드를 정확히 입력하여 USER 권한이 지급되었어요!", timestamp=message.created_at,
            colour=discord.Colour.green()
    )
            embed.set_footer(text="S원라인 인증 도우미", icon_url="https://media.discordapp.net/attachments/735766686090788874/759404838404227072/e6f11eee6427bcbd.png")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.author.guild.roles, name='🐥ㅣ시민')
            await message.author.add_roles(role)
        
        else:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증코드가 올바르지 않아요! 다시 시도해봐요.", timestamp=message.created_at,
            colour=discord.Colour.red()
    )
            embed.set_footer(text="음.. 다시 해봐요", icon_url="https://cdn.discordapp.com/avatars/736135672842420326/79ee3eb1c9e30f6f3f61562e45c02274.webp?size=1024")
            await message.channel.send(embed=embed)
            

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)


