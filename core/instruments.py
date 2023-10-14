from midi.constants import *


class Instrument:
    inst_count = 0

    def __init__(self, name, offset, character):
        self.name = str(Instrument.inst_count) + '_' + name
        Instrument.inst_count += 1
        self.offset = offset
        self.character = character


class MelodicInstrument(Instrument):

    def __init__(self, name, offset):
        super().__init__(name, offset, 'melo')


class PercussiveInstrument(Instrument):

    def __init__(self, name, offset):
        super().__init__(name, offset, 'perc')


class HighStrings(MelodicInstrument):

    def __init__(self):
        super().__init__("high_strings", MID_OFFSET)


class LowStrings(MelodicInstrument):

    def __init__(self):
        super().__init__("low_strings", BASS_OFFSET)


    