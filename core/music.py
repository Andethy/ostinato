from core.gpt.prompts import *
from core.gpt.responses import Responder
from core.instruments import HighStrings, LowStrings
from core.midi.score import Score
from midi.constants import *

class Song:

    def __init__(self, key, tempo, chaos, tracks):
        self.tempo = tempo
        self.key = key
        self.chaos = chaos
        self.tracks = tracks
        self.score = Score()
        self.prompts = PromptManager()
        self.responder = Responder(self.prompts)

    def compose_track(self, track_name):
        pass

    def write_ostinato(self):
        pass


class Waltz(Song):

    def __init__(self, key, tempo, *args, **kwargs):
        super().__init__(key, tempo, 0.5, (HighStrings(), LowStrings()))

    def compose_track(self, instrument):
        instrument = self.tracks[0]
        offset = instrument.offset
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
                    track.append(TONICS_STR[trackname[i]] * count)
                    print(TONICS_STR[trackname[i]])
                
            else:
                count = count + 1
                if trackname[i] != "X":
                    track.append(TONICS_STR[trackname[i]] * count)
                
        print(track)
    compose_track("self", "asd")

    def write_ostinato(self):
        pass

    def create_section(self):
        pass
