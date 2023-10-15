from core.audio.constants import ticks_to_ms
from core.audio.file import MP3File
from core.constants import PATH_TO_MID, PATH_TO_MP3
from core.gpt.prompts import *
from core.gpt.responses import Responder
from core.instruments import HighStringsPizzicato, LowStringsStaccato, HighStringsStaccato
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
        self.mp3File = MP3File(length=track_length + 5000)
        self.prompter = PromptManager()
        self.responder = Responder(self.prompter)
        self.song_complete = False

    def compose_song(self):
        pass

    def write_ostinato(self):
        pass


class Waltz(Song):

    def __init__(self, root, emotion, tempo, chaos=0.5, *args, **kwargs):
        self.measures = 8
        inst1 = HighStringsStaccato() if chaos > 0.5 else HighStringsPizzicato
        super().__init__(root, emotion, tempo, chaos,
                         (inst1, LowStringsStaccato()), ticks_to_ms(self.measures * 3, tempo))

    def compose_song(self):
        self.compose_track(0)
        self.midFile.add_notes(self.score())
        self.midFile.save_file(PATH_TO_MID)
        self.mp3File.add_samples(self.score(), self.tracks, self.tempo)
        self.mp3File.export_file(PATH_TO_MP3)

    def compose_track(self, inst_index):
        inst = self.tracks[inst_index]
        self.score.add_track(inst.name)
        self.midFile.add_tracks([self.score.get_last_track()])
        self.mp3File.add_tracks([self.score.get_last_track()])

        self.prompter.prompts['ost1'] = OstinatoPrompt(self.root, self.emotion, 6)
        flag = False
        response1 = None
        while not flag:
            response1_pre = self.responder.get_response('ost1')
            response1_post = self.prompter.parse_prompt_by_name('ost1', response1_pre)
            print("OSTINATO RESPONSE:", response1_post)
            if len(response1_post.split('|')) == 6:
                flag = True
                response1 = response1_post
        print(response1)
        ost1 = self.make_ostinato(inst, response1)

        print(ost1)
        measures = Measure.create_duplicate_measures(ost1, 16)
        print("NOTES: ", measures[1].get_notes())
        self.score.add_to_track(inst.name, measures)
        for measure in self.score.get_tracks()[0].get_measures():
            for note in measure.get_notes():
                print("FINAL TIME:", note.time)
        print(self.score())

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

    def make_chord(self, note):
        chord = HARMONIES["major-triad"]
        if "m" in note:
            chord = HARMONIES["minor-triad"]
            note = note[:-1]
        chord = list(chord)
        value = TONICS_STR[note]
        for i in range(len(chord)):
            chord[i] += value
        placeholder = [[0], [], [1, 2], [], [1, 2], []]
        for x in range(len(placeholder)):
            for y in range(len(placeholder[x])):
                placeholder[x][y] = chord[placeholder[x][y]]
        print(placeholder)

    def create_section(self):
        pass


if __name__ == '__main__':
    waltz = Waltz("G#", "happy", 60, 0.7)
    waltz.compose_song()
