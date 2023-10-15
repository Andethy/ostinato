from pathlib import Path

from midiutil import MIDIFile as Midi

from midi.score import Track


class MIDIFile:
    def __init__(self, name='output', num_tracks=1):
        self.name = name
        self.file = Midi(num_tracks)

    def add_tracks(self, tracks):
        for index, track in enumerate(tracks):
            self.file.addTrackName(index, 0, track.name)

    def add_note(self, note):
        """


        :type note: Note
        """
        self.file.addNote(*note())

    def add_notes(self, notes):
        """

        :type notes: list
        """
        for note in notes:
            self.add_note(note)

    def save_file(self, file_path):
        # full_path = Path(file_path, 'output.midi') if '.' not in file_path else file_path
        full_path = file_path + name + '.mid'
        with open(full_path, "wb") as out:
            self.file.writeFile(out)


if __name__ == '__main__':
    file = MIDIFile('test1', 2)
    file.add_tracks([Track("0_test"), Track("1_test")])
