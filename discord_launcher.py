##HEELLOO U NERDS
import discord
from discord.ext import commands
import random
## Flippity Floppity, hers your note-opity
global noteList
noteList = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
global minor
minor = [2,1,2,2,1,2,2]
global major
major = [2,2,1,2,2,2,1]

def keys(note, length):
    fuck = []
    if "m" in note:
        note = note[:note.index("m")] 
        count = noteList.index(note)
        if length == 1:
            fuck.append(noteList[count+2])
        else:    
            for x in minor[:length]:
                fuck.append(noteList[count])
                count += x
    else:
        count = noteList.index(note)
        if length == 1:
            fuck.append(noteList[count+2])
        else:    
            for x in major[:length]:
                fuck.append(noteList[count])
                count += x
    return fuck

description = '''lel idk what im doing :D'''
bot = commands.Bot(command_prefix='#', description=description)
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
bot.run('NTY0OTU5MzQ2MTY1ODA5MTU5.XKvu6A.HQcTacWF1pA6GznSze6c596I68Y')
