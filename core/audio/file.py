import os.path
import random
from datetime import datetime

from pydub import AudioSegment
from pydub.playback import play

from core.constants import find_root_folder
from core.audio.constants import ticks_to_ms


class MP3Stem:

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.audio = AudioSegment.silent(length)

    def encode_sample(self, note, instrument, tempo):
        path = instrument.get_sample_path(note.value)
        sound = AudioSegment.from_mp3(os.path.join(find_root_folder('resources', os.getcwd(), 0).replace('api/', '').replace('core/', ''), path))
        self.audio = self.audio.overlay(sound, ticks_to_ms(note.time, tempo))


class MP3File:
    #stems: list[MP3Stem]

    def __init__(self, name='output', length=0):
        self.name = name
        self.path = ''
        self.length = length
        self.stems = []

    def add_tracks(self, midi_tracks):
        for track in midi_tracks:
            self.stems.append(MP3Stem(track.name, self.length))

    def add_samples(self, notes, instruments, tempo):
        for note in notes:
            index = note.track
            self.stems[index].encode_sample(note, instruments[index], tempo)

    def export_file(self, path):
        base = AudioSegment.silent(self.length)
        for stem in self.stems:
            # if "high" in stem.name:
            #     print("INCR HIGH GAIN")
            #     stem.audio = stem.audio.apply_gain(12.)
            if "pizz" in stem.name:
                print("INCR PIZZ GAIN")
                stem.audio = stem.audio.apply_gain(3.)
            if "low" in stem.name:
                print("DECR LOW GAIN")
                stem.audio = stem.audio.apply_gain(-4.5)
            base = base.overlay(stem.audio, 0)
        base = base.apply_gain(4.5)
        # play(base)
        self.name = self.name + datetime.now().strftime("-%Y_%m_%d-%H_%M_%S-") + str(random.randint(10, 100))
        self.path = path + f'{self.name}.mp3'
        base.export(self.path)
