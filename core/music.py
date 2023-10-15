from core.gpt.prompts import *
from core.gpt.responses import Responder
from core.instruments import HighStrings, LowStrings
from core.midi.score import Score
from midi.constants import *
from instruments import *

class Song:

    def __init__(self, key, tempo, chaos, tracks, gpt_api_key=None):
        self.tempo = tempo
        self.key = key
        self.chaos = chaos
        self.tracks = tracks
        self.score = Score()
        self.prompts = PromptManager()
        self.responder = Responder(self.prompts)
        self.song_complete = False

    def compose_track(self, track_name):
        pass

    def write_ostinato(self):
        pass


class Waltz(Song):

    def __init__(self, key, tempo, *args, **kwargs):
        super().__init__(key, tempo, 0.5, (HighStrings(), LowStrings()))

    def compose_track(self, instrument):
        offset = INST_DICT[instrument]
        track_name = "E|F#|G|B|E|X"
        trackname = track_name.split('|')
        print(trackname)
        track = []
        for i in range(len(trackname)):
            count = 1
            if i!= len(trackname)-1:
                while trackname[i] == trackname[i+1]:
                    i+=1
                    count = count + 1
                if trackname[i] != "X":
                    track.append((TONICS_STR[trackname[i]]+offset) * count)
                    print(TONICS_STR[trackname[i]])     
            else:
                count = count + 1
                if trackname[i] != "X":
                    track.append((TONICS_STR[trackname[i]]+offset) * count)
               
        print(track)
    #compose_track("self", "high_strings")

    def make_ostinato(self):
        pass

    def make_chord(self, note):
        chord = HARMONIES["major-triad"]
        if "m" in note:
            chord = HARMONIES["minor-triad"] 
            note=note[:-1]
        chord = list(chord)
        value = TONICS_STR[note]
        for i in range(len(chord)):
            chord[i] += value
        placeholder= [[0],[],[1,2],[],[1,2],[]]
        for x in range(len(placeholder)):
            if placeholder[x] != []:
                for y in range(len(placeholder[x])):
                    placeholder[x][y] = chord[placeholder[x][y]]
        print(placeholder)
    
    def create_section(self):
        pass

    if __name__ == '__main__' :
        pass

