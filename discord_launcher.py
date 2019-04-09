##HEELLOO U NERDS
import discord
from discord.ext import commands
import random
## Flippity Floppity, hers your note-opity
noteList = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
### Minors 2 1 2 2 1 2 2
### Majors 2 2 1 2 2 2 1
description = '''I will make your music less shit'''
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
    if 'm' in note and len(note) > 2:
        tempnote = note[:2]
        print(len(note))
    elif 'm' in note and len(note) == 2:
        tempnote = note[0]
        print(len(note))
    else:
        tempnote = note
    if tempnote in noteList:
        rList = []
        if 'm' not in note:
            print('major')
            print(tempnote)
            setpos = noteList.index(tempnote)
            counter = 0
            number = setpos
            if length == 1:
                if 'b' in noteList[number+1]:
                    rList.append(noteList[number+2])
                else:
                    rList.append(noteList[number+2])
            else:
                while counter != length:
                    if counter == 2 or counter == 6:
                        number += 1
                        rList.append(noteList[number])
                        counter += 1
                    else:
                        number += 2
                        rList.append(noteList[number])
                        counter += 1
        else:
            print('minor')
            print(tempnote)
            setpos = noteList.index(tempnote)
            counter = 0
            number = setpos
            if length == 1:
                if 'b' in noteList[number+1]:
                    rList.append(noteList[number+2])
                else:
                    rList.append(noteList[number+2])
            else:
                while counter != length:
                    if counter == 1 or counter == 4:
                        number += 1
                        rList.append(noteList[number])
                        counter += 1
                    else:
                        number += 2
                        rList.append(noteList[number])
                        counter += 1

        solution = 'Next note in this key is:  '+str(rList)
    else:
        solution = "Couldn't find your Note: "+note+", please remember, the syntax is #key <starting note> length"
    await ctx.send(solution)
bot.run('Hello put a key in me :D')
