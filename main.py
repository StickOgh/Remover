import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Streaming(name='streaming-Ian On Top', url='https://discord.com/invite/FZxbnmJCx6'))

bot.run('MTIxMjM2NDA5ODM5NDY2MDkxNQ.GaqoZ3.b6_PaiY-i9BO8Eoih2wtWAGsy5sORJFQbwCUfI')
