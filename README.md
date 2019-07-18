🎵 Welcome to Tempo 🎵

Tempo is a Discord bot made entirely on Python 3.7.3

Tempo was made by Music lovers, for Music lovers.

Tempo will show you (and any users) different Musical Theory for whichever note you throw at it.

Requirements:
 - Discord.py
 - Discord.py[voice]
<<<<<<< HEAD
=======
 - ffmpeg
 - Python 3.7.3
 
 Usage
  - #Key <Key> <length>
    - Note - The note you are starting on:  Cm / C
    - Length - How many notes you want shown (default 1, max 7)
  - #prog <note> <length>
    - Key - The Key you want
    - Length - How long is your progression?
	#prog also has Voice chat support!
		- if user is in voice chat, Tempo will join and play your notes to you!
  - #chord <root-note> <chord Type> <delta> <length>
    - root-note - the Root note in the chord
    - chord Type - Major? Minor? Augmented? Diminish? defaults to major.
    - Delta - Is your chord a 7th? 13th? only 7th is working as of 4/17/2019
    - length - Replaces with delta, haven't made necessary adjustments.
   
Too add Tempo to your server, use the following link:
https://discordapp.com/api/oauth2/authorize?client_id=564959346165809159&permissions=36760832&scope=bot