import discord
import asyncio

############# 중요한 부분 #############

prefix = "!" #봇의 접두사

asygame1 = discord.Game("원라인 서버 인증") #봇의 상태메세지

hasrole = "510440718217642001" #명령어를 사용할 수 있는 역할

youanot = "당신은 사용할 권한이 없습니다." #권한이 없는 멤버에게 표시될 말

giverole = "692408623892135947" #인증 대상에게 주어질 역할

access_token = os.environ["BOT_TOKEN"]
client.run(access_token) #봇 토큰

####################################


class chatbot(discord.Client):
    async def on_ready(self):
        print("봇 ON")
        await client.change_presence(status=discord.Status.online, activity=asygame1)
        
    async def on_message(self, message):
        if message.content.startswith(prefix + "인증"):
            user = message.author
            if discord.utils.get(user.roles, name=hasrole):
                author = message.guild.get_member(message.mentions[0].id)
                role = discord.utils.get(message.guild.roles, name=giverole)
                await author.add_roles(role)
                response = "인증이 정상적으로 처리 되었습니다. \n 인증 받으신 분 : **" + str(message.mentions[0]) + "**"
                hoho = "명령어 사용자 : " + message.author.name
                embed = discord.Embed(title=":OneLine1: UCCESFUL 성공", description=response, timestamp=message.created_at, color=0xf787d4)
                embed.set_footer(text=hoho, icon_url="https://kin-phinf.pstatic.net/20200306_189/1583469080247oiWVd_PNG/dd640b46ae14e40b9706282c5c5b26e2.png?type=w750")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(youanot)
                

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
