import random

class Tempo:
    def __init__(self):
        self.minor = [2,1,2,2,1,2,2]
        self.major = [2,2,1,2,2,2,1]
        self.piano_roll = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        self.piano_auctave=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

    def getKeyScale(self, note_and_key):
        '''
        keys(Note_Key, How long you want returned(MAX 7))
        This function returns the musical key.
        '''
        key_list = []
        note_and_key = note_and_key.lower()
        if "min" in note_and_key:
            note = (note_and_key.split("min")[0].upper()).replace(' ','')
            step = self.piano_roll.index(note)
            for i in range(len(self.minor)):
                key_list.append(self.piano_roll[step])
                step += self.minor[i]
        elif "maj" in note_and_key:
            note = (note_and_key.split("maj")[0].upper()).replace(' ','')
            step = self.piano_roll.index(note)
            for i in range(len(self.minor)):
                key_list.append(self.piano_roll[step])
                step += self.major[i]
        return key_list

    def octave(self,root):
        root_note = self.piano_roll.index(root.upper())
        octave_list=[]
        counter = 0
        while counter != 12:
            octave_list.append(self.piano_roll[root_note+counter])
            counter += 1
        return octave_list

    def getNoteProg(self,key,length=3):
        progression_list = []
        if length > 7:
            length = 7
        if 'min' not in key and 'maj' not in key:
            key += 'maj'
        key_list = self.getKeyScale(key)
        counter = 0
        while counter != length:
            random_note = key_list[random.randint(0,len(key_list)-1)]
            if random_note in progression_list:
                pass
            else:
                progression_list.append(random_note)
                counter +=1
        return progression_list

    def generateChordProgression(self,key,length=3):
        major_steps=[4,3,4,3,4,3]
        minor_steps=[3,4,3,4,3,4]
        augmented_steps=[4,4,4,4,4]
        diminished_steps=[3,3,3,3,3]
        chord = []
        count= 0
        if 'min' in key:
            note = ((key.split("min")[0].upper()).replace(' ',''))
            key_list = self.octave(note)
            for i in minor_steps:
                chord.append(key_list[count])
                count += i
                if count >= len(key_list):
                    count -= len(key_list)
                if len(chord) == length:
                    break
        elif "maj" in key:
            note = ((key.split("maj")[0].upper()).replace(' ',''))
            key_list = self.octave(note)
            chord = []
            count= 0
            for i in major_steps:
                chord.append(key_list[count])
                count += i
                if count >= len(key_list):
                    count -= len(key_list)
                if len(chord) == length:
                    break
        elif "aug" in key:
            note = ((key.split("aug")[0].upper()).replace(' ',''))
            key_list = self.octave(note)
            for i in augmented_steps:
                chord.append(key_list[count])
                count += i
                if count >= len(key_list):
                    count -= len(key_list)
                if len(chord) == length:
                    break
        elif "dim" in key:
            note = ((key.split("dim")[0].upper()).replace(' ',''))
            key_list = self.octave(note)
            for i in diminished_steps:
                chord.append(key_list[count])
                count += i
                if count >= len(key_list):
                    count -= len(key_list)
                if len(chord) == length:
                    break
        return chord

    def findKeyFromNotes(self,note_list):
        temp_dict_maj ={}
        temp_dict_min ={}
        for i in self.piano_auctave:
            temp_dict_maj[i] = 0
            temp_dict_min[i] = 0
        for i in self.piano_auctave:
            for j in self.getKeyScale(i+'maj'):
                if j in note_list:
                    temp_dict_maj[i]+=1
            for j in self.getKeyScale(i+'min'):
                if j in note_list:
                    temp_dict_min[i]+=1
        start_val= 0
        temp =''
        temp_m = 'maj'
        for i in temp_dict_maj:
            if temp_dict_maj[i] > start_val:
                start_val = temp_dict_maj[i]
                temp=i
                temp_m = 'maj'
        for i in temp_dict_min:
            if temp_dict_min[i] > start_val:
                start_val = temp_dict_maj[i]
                temp=i
                temp_m = 'min'
        temp=temp+' '+temp_m
        return temp
