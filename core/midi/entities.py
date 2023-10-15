from core.midi.constants import *


class Note:
    def __init__(self,
                 value: int,
                 duration: float = 4.,
                 time: float = 0.,
                 velocity: int = 75,
                 track: str = '0',
                 channel: int = 0,
                 annotation: object = None) -> None:
        self.track = track
        self.channel = channel
        self.value = value
        self.time = time
        self.duration = duration
        self.velocity = velocity
        self.annotation = annotation

    def __call__(self, *args, **kwargs):
        """
        Call this method anytime you want to output the arguments

        :return: tuple of the arguments required for the addNote() method
        """
        return self.track, self.channel, self.value, self.time, self.duration, self.velocity, self.annotation

    def __str__(self):
        return self.get_note_value()

    def get_note_value(self):
        return TONICS_INT[self.value % 12] + str(self.value // 12 - 2)

    def assign_track(self, track_name):
        self.track = track_name

    def offset_position(self, position):
        self.time += position

class Chord:
    def __init__(self, *args: Note, root_note="", chord_type=""):
        self._notes = []
        self.root_note = root_note
        self.chord_type = chord_type
        for arg in args:
            self._notes.append(arg) if type(arg) == Note else None
        if root_note and chord_type:
            self._notes = list(Note(TONICS_STR[root_note] + n) for n in HARMONIES[chord_type])



    def __call__(self, *args, **kwargs):
        return tuple(self._notes)
