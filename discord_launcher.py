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
    '''
    keys(Note_Key, How long you want returned(MAX 7))
    This function returns the musical key.
    '''
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

def octave(root):
    '''
    octave(root_note)
    This function returns the 12 notes in an octave'''
    octave_list=[]
    count = noteList.index(root)
    counter= 0 
    for i in noteList:
        if counter >= 12:
            break
        octave_list.append(noteList[count])
        count += 1
        counter += 1
    return octave_list

def progression(keylist,amt):
    '''
    progression(Note Key, How many notes in progression)
    This function returns a random note progression
    '''
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

def chordify(octavelist,noteType,delta,length):
    '''
    chordify(list of entire octave,how many notes in chord)
    this function generates logical chords using the notes in a given octave

    Needs:
        Minors, Augments, Dimishes
    '''
    chordList = []
    count=0
    major_steps=[4,3,4,3,4,3]
    minor_steps=[3,4,3,4,3,4]
    augmented_steps=[4,4,4,4,4]
    diminished_steps=[3,3,3,3,3]
    if 'minor' in noteType:
        for x in minor_steps[:length]:
            if count >= len(octavelist):
                chordList.append(octavelist[count-12])
            else:
                chordList.append(octavelist[count])
                count += x
    elif 'major' in noteType:
        for x in major_steps[:length]:
            if count >= len(octavelist):
                chordList.append(octavelist[count-12])
            else:
                chordList.append(octavelist[count])
                count += x
    elif 'dim' in noteType:
        for x in diminished_steps[:length]:
            if count >= len(octavelist):
                chordList.append(octavelist[count-12])
            else:
                chordList.append(octavelist[count])
                count += x
    elif 'aug' in noteType:
        for x in augmented_steps[:length]:
            if count >= len(octavelist):
                chordList.append(octavelist[count-12])
            else:
                chordList.append(octavelist[count])
                count += x
    else:
        chordList='Hmm, seems like '+noteType+' is not a chord type!  Should check your spelling :eyes:'
    if str(delta) == '7' and type(chordList) == list:
            chordList.append(octavelist[octavelist.index(chordList[-1])+3])
    return chordList

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
        
@bot.command()
async def chord(ctx, root:str,noteType='major',delta=0,length=3,):
    """Bot takes args and generates the logical Triad Note using the Root (unless larger) """
    if length < 2:
        length = 2
    elif length > 5:
        length = 5
    getOctave=octave(root)
    chord = chordify(getOctave,noteType,delta,length)
    await ctx.send(chord)


bot.run('')
