import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import os, random, asyncio, time
global noteList
noteList = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
global minor
minor = [2,1,2,2,1,2,2]
global major
major = [2,2,1,2,2,2,1]

def keys(note, length):
    key_list = []
    if "m" in note:
        note = note[:note.index("m")]
        count = noteList.index(note)
        if length == 1:
            key_list.append(noteList[count+2])
        else:
            for x in minor[:length]:
                key_list.append(noteList[count])
                count += x
    else:
        count = noteList.index(note)
        if length == 1:
            key_list.append(noteList[count+2])
        else:
            for x in major[:length]:
                key_list.append(noteList[count])
                count += x
    return key_list

def progression(keylist,amt):
    answer_list=[]
    if amt <= 0:
        amt = 3
    elif amt >=7:
        amt = 7
    counter = 1
    while counter <= amt:
        potential =random.randint(0,6)
        if keylist[potential] in answer_list:
            pass
        else:
            answer_list.append(keylist[potential])
            counter += 1
    return answer_list


description = '''lel idk what im doing :D'''
bot = commands.Bot(command_prefix='#')
soundList = os.listdir('sounds/')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def key(ctx, note:str,length=1):
    """Bot takes argument,
applies to notes, then gives back notes that sound aight"""
    if length < 1:
        length = 1
    elif length > 7:
        length = 7
    answer=keys(note, length)
    solution = 'Next note in this key is:  '+str(answer)
    await ctx.send(solution)

@bot.command()
async def prog(ctx, note:str,amount=3):
    """Bot takes the key, and amount then generates a random chord progression."""
    k=keys(note,7)
    answer = progression(k,amount)
    solution = 'Generated Key Progression '+str(answer)
    await ctx.send(solution)
    if ctx.author.voice is not None:
        vc = await ctx.author.voice.channel.connect()
        for i in range(len(answer)):
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('sounds/'+str(answer[i])+'.mp3'))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            time.sleep(1)
        await vc.disconnect()


bot.run('')