from pathlib import Path

from core.midi.constants import *
from core.constants import *


class Instrument:
    inst_count = 0

    def __init__(self, name, offset, sample_path, character):
        self.name = str(Instrument.inst_count) + '_' + name
        Instrument.inst_count += 1
        self.offset = offset
        self.character = character
        self.sample_path = sample_path

    def get_sample_path(self, note, ext='mp3'):
        return Path(self.sample_path, str(note) + '.' + ext)


class MelodicInstrument(Instrument):

    def __init__(self, name, offset, path):
        super().__init__(name, offset, path, 'melo')


class PercussiveInstrument(Instrument):

    def __init__(self, name, offset):
        super().__init__(name, offset, None, 'perc')


class HighStringsPizzicato(MelodicInstrument):

    def __init__(self):
        super().__init__("high_strings", MID_OFFSET, 'sounds/high_strings/pizzicato/')


class HighStringsStaccato(MelodicInstrument):

    def __init__(self):
        super().__init__("high_strings", MID_OFFSET, 'sounds/high_strings/staccato/')


class LowStringsStaccato(MelodicInstrument):

    def __init__(self):
        super().__init__("low_strings", BASS_OFFSET, 'sounds/low_strings/staccato/')
