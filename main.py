import discord
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
import asyncio
import time

client = commands.Bot(command_prefix = '??')

@client.event
async def on_readt():
    print("Il bot è pronto all uso dio cane")
    print("----------------------------------")


@client.command()
async def ciao(ctx):
    await ctx.send("Ti piace il cazzo")


@client.command(pass_context = True)
async def entra(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('wenegri.mp3')
        player = voice.play(source)

    else:
        await ctx.send("Devi entrare nel canale vocale dio santo")


@client.command(pass_context = True)
async def smetti(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.stop()

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

@client.command(pass_context = True)
async def esci(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('quit.mp3')
        player = voice.play(source)
    while voice.is_playing():
        await asyncio.sleep(1) 
    else:
        await asyncio.sleep(1) 
    while voice.is_playing():
        break 
    else:
        await voice.disconnect() 


@client.command(pass_context = True)
async def animaon(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('niente.mp3')
        player = voice.play(source)
    while voice.is_playing():
         await asyncio.sleep(20)
         channel = ctx.message.author.voice.channel
         voice = ctx.guild.voice_client
         source = FFmpegPCMAudio('poverino.mp3')
         player = voice.play(source)
         await asyncio.sleep(15)
         channel = ctx.message.author.voice.channel
         voice = ctx.guild.voice_client
         source = FFmpegPCMAudio('niente.mp3')
         player = voice.play(source)
         await asyncio.sleep(10)
         channel = ctx.message.author.voice.channel
         voice = ctx.guild.voice_client
         source = FFmpegPCMAudio('madre.mp3')
         player = voice.play(source)
    
   






@client.command(pass_context = True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg + '.mp3')
    player = voice.play(source)



client.run('ODMxOTUwMjU1Mzk3MjczNjAw.YHcsDQ.BtmwLmKjGOIYlkf2bMWzg-57se4')