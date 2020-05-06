import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE - Olá mundo!')
    print(client.user.name)
    print(client.user.id)

@client.event

async def on_message(message):
    if message.content.lower().startswith('.ola'):
        await message.channel.send('OLÁ ^^')

    if message.content.lower().startswith('.moeda'):
        await message.channel.send('din din')

    if message.content.lower().startswith('.live'):
        await message.channel.send('https://twitch.tv/br_gepeto')
#.live faz o bot mandar o link da twitch no chat!!

    if message.content.lower().startswith('.caracoroa'):
            escolha = random.randint(1, 2)
            if escolha == 1:
                await message.channel.send('😀')
            if escolha == 2:
                await message.channel.send('👑')

client.run('TOKEN')
