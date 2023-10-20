import copy
from random import random

from core.audio.constants import ticks_to_ms
from core.audio.file import MP3File
from core.constants import PATH_TO_MID, PATH_TO_MP3
from core.gpt.prompts import *
from core.gpt.responses import Responder
from core.instruments import HighStringsPizzicato, LowStringsStaccato, HighStringsStaccato, LowStringsPizzicato, \
    Instrument
from core.midi.score import Score, Measure
from core.midi.constants import *
from core.midi.file import MIDIFile


class Song:

    def __init__(self, root, emotion, tempo, chaos, tracks, track_length, gpt_api_key=None):
        self.tempo = tempo
        self.root = root
        self.emotion = emotion
        self.chaos = chaos
        self.tracks = tracks
        self.score = Score()
        self.midFile = MIDIFile(num_tracks=len(tracks))
        self.mp3File = MP3File(length=track_length + 1500)
        self.prompter = PromptManager()
        self.responder = Responder(self.prompter)
        self.song_complete = False

    def compose(self):
        pass

    def write_ostinato(self):
        pass

    @staticmethod
    def make_ostinato(inst, notes):
        offset = inst.offset
        notes_split = notes.split('|')
        print(notes_split)
        ostinato_notes = []
        for i in range(len(notes_split)):
            if notes_split[i] == '':
                continue
            count = 1
            ostinato_notes.append([])
            if i != len(notes_split) - 1:
                while notes_split[i] == notes_split[i + 1]:
                    pass
                    # i += 1
                    # count = count + 1
                if notes_split[i] != "X":
                    ostinato_notes[len(ostinato_notes) - 1].append((TONICS_STR[notes_split[i]] + offset))
                    print(TONICS_STR[notes_split[i]])
            else:
                # count = count + 1
                if notes_split[i] != "X":
                    ostinato_notes[len(ostinato_notes) - 1].append((TONICS_STR[notes_split[i]] + offset))

            # if i > 0:
            #     if ostinato_notes[len(ostinato_notes) - 1][0] + 12 < ostinato_notes[len(ostinato_notes) - 2][0]:
            #         ostinato_notes[len(ostinato_notes) - 1] += 12
            #     elif ostinato_notes[len(ostinato_notes) - 1][0] - 12 > ostinato_notes[len(ostinato_notes) - 2][0]:
            #         ostinato_notes[len(ostinato_notes) - 1] -= 12
        return ostinato_notes

    def make_chord(self, inst, root):

        chord = HARMONIES['major-triad']
        if "m" in root:
            chord = HARMONIES['minor-triad']
            root = root[:-1]
        chord = list(chord)
        value = TONICS_STR[root]
        for i in range(len(chord)):
            chord[i] += value
        acc = ACCOMPANIMENTS['waltz']
        chord_map = copy.deepcopy(acc[int(25 * self.chaos * random()) % len(acc)])
        for x in range(len(chord_map)):
            for y in range(len(chord_map[x])):
                chord_map[x][y] = chord[chord_map[x][y]] + inst.offset
        return chord_map


class Waltz(Song):
    # manager.py line 19 passes in the following arguments to the Waltz constructor.
    # self.song = Waltz(key_signature, emotion, tempo, chaos_factor) #waltz takesgpt api keytracks, key and tempo for now.
    def __init__(self, root, emotion, tempo, chaos=0.5, *args, **kwargs):
        Instrument.inst_count = 0
        self.measures = 8
        inst1 = HighStringsStaccato() if chaos + random() * 0.5 > 1. else HighStringsPizzicato()
        inst2 = LowStringsStaccato() if chaos + random() * 0.5 > 1.25 else LowStringsPizzicato()
        if chaos + random() > 0.8:
            inst1.offset += 12
        if chaos + random() > 1.1:
            inst2.offset -= 12

        super().__init__(root, emotion, tempo, chaos,
                         (inst1, LowStringsStaccato()), ticks_to_ms(self.measures * 3, tempo))

    def compose(self):
        self.compose_track1(0)
        self.compose_track2(1)
        self.midFile.add_notes(self.score())
        self.midFile.save_file(PATH_TO_MID)
        self.mp3File.add_samples(self.score(), self.tracks, self.tempo)
        self.mp3File.export_file(PATH_TO_MP3)
        self.song_complete = True

    def compose_track1(self, inst_index):
        inst = self.tracks[inst_index]
        self.score.add_track(inst.name)
        self.midFile.add_tracks([self.score.get_last_track()])
        self.mp3File.add_tracks([self.score.get_last_track()])

        self.prompter.prompts['ost1'] = StandardOstinatoPrompt("waltz", self.root, self.emotion, 6)
        flag = False
        response1 = None
        while not flag:
            response1_pre = self.responder.get_response('ost1')
            response1_post = self.prompter.parse_prompt_by_name('ost1', response1_pre)
            print("GPT RESPONSE:", response1_post)
            if len(response1_post.split('|')) == 6:
                flag = True
                response1 = response1_post
        print(response1)
        ost1 = self.make_ostinato(inst, response1)

        print(ost1)
        measures = Measure.create_duplicate_measures(ost1, 8)
        print("NOTES: ", measures[1].get_notes())
        self.score.add_to_track(inst.name, measures)
        print(self.score())

    def compose_track2(self, inst_index):
        inst = self.tracks[inst_index]
        self.score.add_track(inst.name)
        self.midFile.add_tracks([self.score.get_last_track()])
        self.mp3File.add_tracks([self.score.get_last_track()])

        # self.prompter.prompts['ch1'] = Prompt(self.root, self.emotion, 6)

        ch1 = self.make_chord(inst, self.root + 'm' if self.emotion == 'dramatic' else self.root)

        print(ch1)
        measures = Measure.create_duplicate_measures(ch1, 8)
        print("NOTES: ", measures[1].get_notes())
        self.score.add_to_track(inst.name, measures)
        print(self.score())

    def create_section(self):
        pass


class Action(Song):

    def __init__(self, root, emotion, tempo, chaos=0.5, *args, **kwargs):
        Instrument.inst_count = 0
        self.measures = 8
        inst1 = HighStringsStaccato()
        inst2 = LowStringsStaccato()
        super().__init__(root, emotion, tempo, chaos,
                         (inst1, inst2), ticks_to_ms(self.measures * 4, tempo))


if __name__ == '__main__':
    waltz = Waltz("F#", "happy", 180, 0.45)
    waltz.compose()
