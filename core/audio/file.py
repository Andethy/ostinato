import os.path
from typing import List, Any

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
        sound = AudioSegment.from_mp3(os.path.join(find_root_folder('resources', os.getcwd(), 0).replace('/core', ''), path))
        self.audio = self.audio.overlay(sound, ticks_to_ms(note.time, tempo))


class MP3File:
    stems: list[MP3Stem]

    def __init__(self, name='output', length=0):
        self.name = name
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
            stem.audio.apply_gain(24.)
            base = base.overlay(stem.audio, 0)
        base.apply_gain(18.0)
        play(base)
        base.export(path + f'/{self.name}.mp3')
