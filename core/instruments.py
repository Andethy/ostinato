from midi.constants import *


class Instrument:
    inst_count = 0

    def __init__(self, name, offset):
        self.name = str(Instrument.inst_count) + '_' + name
        Instrument.inst_count += 1
        self.offset = offset


class HighStrings(Instrument):

    def __init__(self):
        super().__init__("high_strings", MID_OFFSET)


class LowStrings(Instrument):

    def __init__(self):
        super().__init__("low_strings", BASS_OFFSET)
