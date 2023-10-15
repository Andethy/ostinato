from core.gpt.prompts import *
from core.gpt.responses import Responder
from core.instruments import HighStrings, LowStrings
from core.midi.score import Score
from midi.constants import *

class Song:

    def __init__(self, root, emotion, tempo, chaos, tracks, gpt_api_key=None):
        self.tempo = tempo
        self.root = root
        self.emotion = emotion
        self.chaos = chaos
        self.tracks = tracks
        self.score = Score()
        self.prompter = PromptManager()
        self.responder = Responder(self.prompter)
        self.song_complete = False

    def compose_track(self, track_name):
        pass

    def write_ostinato(self):
        pass


class Waltz(Song):

    def __init__(self, root, emotion, tempo, *args, **kwargs):
        super().__init__(root, emotion, tempo, 0.5, (HighStrings(), LowStrings()))

    def compose_track(self, inst_index):
        self.prompter.prompts['ost1'] = OstinatoPrompt(self.root, self.emotion, 6)
        response1_pre = self.responder.get_response('ost1')
        response1_post = self.prompter.parse_prompt_by_name('ost1', response1_pre)
        print("OSTINATO RESPONSE:", response1_post)
        self.make_ostinato(inst_index, response1_post)

    def make_ostinato(self, inst_index, notes):
        inst = self.tracks[inst_index]
        offset = inst.offset
        notes_split = notes.split('|')
        print(notes_split)
        track = []
        for i in range(len(notes_split)):
            count = 1
            track.append([])
            if i != len(notes_split) - 1:
                while notes_split[i] == notes_split[i + 1]:
                    i += 1
                    # count = count + 1
                if notes_split[i] != "X":
                    track[len(track) - 1].append((TONICS_STR[notes_split[i]] + offset))
                    print(TONICS_STR[notes_split[i]])
            else:
                # count = count + 1
                if notes_split[i] != "X":
                    track[len(track) - 1].append((TONICS_STR[notes_split[i]] + offset))

        print(track)

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
            for y in range(len(placeholder[x])):
                placeholder[x][y] = chord[placeholder[x][y]]
        print(placeholder)
    
    def create_section(self):
        pass


if __name__ == '__main__':
    waltz = Waltz("E","sad", 120)
    waltz.compose_track(0)