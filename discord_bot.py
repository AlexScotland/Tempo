from functionClass import Tempo
import discord, os, random, asyncio, time
from discord.ext import commands
from discord.voice_client import VoiceClient
from pydub import AudioSegment
from pydub.playback import play

Tempo = Tempo()
description = '''Tempo is Discord's First music-theory bot!'''
bot = commands.Bot(command_prefix='#')
soundList = os.listdir('sounds/')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def key(ctx, note:str, length=7):
    """Bot takes argument,
applies to notes, then gives back notes that sound aight"""
    if length < 1:
        length = 1
    elif length > 7:
        length = 7
    answer=Tempo.getKeyScale(note)
    solution = 'Next notes in this key is:  '+str(answer)
    await ctx.send(solution)

@bot.command()
async def prog(ctx, note:str,amount=3):
    """Bot takes the key, and amount then generates a random chord progression."""
    answer = Tempo.getNoteProg(note,amount)
    solution = 'Generated Key Progression '+str(answer)
    await ctx.send(solution)
    if ctx.author.voice is not None:
        vc = await ctx.author.voice.channel.connect()
        for i in range(len(answer)):
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('sounds/'+str(answer[i])+'.mp3'))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            time.sleep(1)
        await vc.disconnect()
        
@bot.command()
async def chord(ctx, root:str,length=3,):
    """Bot takes args and generates the logical Triad Note using the Root (unless larger) """
    if length < 2:
        length = 2
    elif length > 5:
        length = 5
    chord = Tempo.generateChordProgression(root)
    await ctx.send(chord)



