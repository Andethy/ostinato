from midi.constants import *


class Instrument:

    def __init__(self, offset):
        self.offset = offset


class HighStrings(Instrument):

    def __init__(self):
        super().__init__(MID_OFFSET)


class LowStrings(Instrument):

    def __init__(self):
        super().__init__(BASS_OFFSET)
