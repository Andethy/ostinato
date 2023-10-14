import math
from entities import *
from constants import *


class KeySignature:
    def __init__(self, root: str, scale: str):
        self.root = root
        self.scale = scale
        self._root = TONICS_STR[root]
        self._scale = SCALES[scale]

    def get_relative_scale(self):
        return self._scale

    def get_key(self):
        return tuple(self._root + n for n in self._scale)


class TimeSignature:
    def __init__(self, time, clocks_per_tick=24, notes_per_quarter=8):
        """
        :param time: time signature in the format "[NUMBER]/[NUMBER]"
        :type time: str
        """
        self._time = time
        self._numerator, self._denominator = int(time.split('/')[0]), math.log2(int(time.split('/')[1]))
        self._clocks_per_tick = clocks_per_tick
        self._notes_per_quarter = notes_per_quarter

    def __call__(self, *args, **kwargs):
        return self._time, self._numerator, self._denominator, self._clocks_per_tick, self._notes_per_quarter


class Measure:
    def __init__(self, *args, key_switch=None, time_switch=None):
        self._entities = []
        for arg in args:
            self.add_entity(arg)
        self._key_switch = key_switch
        self._time_switch = time_switch

    def add_entity(self, entity):
        self._entities.append(entity) if type(entity) in (Note, Chord) else None

    def is_blank(self):
        return len(self._entities) == 0

    def get_notes(self):
        """

        :rtype: list[Note]
        """
        notes = []
        for entity in self._entities:
            if type(entity) == Chord:
                for note in entity():
                    notes.append(note)
            elif type(entity) == Note:
                notes.append(entity)
        return notes


class Track:
    _measures: list[Measure]

    def __init__(self, name):
        self._name = name
        self._measures = []
        self._pen = -1

    def append_measures(self, number=1):
        for n in range(number):
            self._measures.append(Measure())

    def set_pen(self, number=0, auto=False):
        if auto:
            for index, measure in enumerate(self._measures):
                if measure.is_blank():
                    self._pen = index
                    break
        else:
            self._pen = number

    def add_at_measure(self, measure, *args):
        self.set_pen(auto=True) if measure == -1 else self.set_pen(number=measure)
        try:
            for arg in args:
                self._measures[measure].add_entity(arg)
        except IndexError:
            print(f"Measure number {measure} is out of range of the score.")

    def assign_notes_to_track(self):
        for index, measure in enumerate(self._measures):
            for note in measure.get_notes():
                note.assign_track(self._name)
                note.offset_position(index * 4.0)


class Score:
    _tracks: list[Track]

    def __init__(self):
        self._tracks = []
        self._writer_number = -1

    def add_track(self, name):
        self._tracks.append(Track(name))

    def set_writer(self, number):
        try:
            self._tracks[number].append_measures(0)
        except IndexError:
            print(f"Invalid track number {number}.")

    def write(self, *items, measure_number=-1):
        if self._writer_number == -1:
            return None
        self._tracks[self._writer_number].add_at_measure(measure_number, *items)

    def get_index_by_name(self, track_name):
        return self._tracks.index(track_name)


if __name__ == '__main__':
    score = Score()
    score.add_track('test')
    score.write()