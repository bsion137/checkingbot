# -*- coding:utf-8 -*-
import discord
import asyncio

token = "Nzk0NTE2OTUyMjMxMDUxMjc0.X-79kg.fk7efxw8tZSLAxZ_kxANCApi_Mc"
client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("출석체크는 언제나 환영입니다"))
  print("봇 실행완료")
  print(client.user.name)
  print(client.user.id)

@client.event
async def on_message(message):
  if message.author.bot:
      return None
  if message.content == "!출석체크":
    await message.channel.send(f"{message.author.mention} 님의 출석체크가 완료되었습니다")


client.run(token)
