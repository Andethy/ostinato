from pathlib import Path
from core.music import Waltz


class CoreManager:

    def __init__(self):
        self.song = None

    def pass_request(self, tempo, genre, chaos_factor, key_signature, emotion) -> int:
        """
        Passes in form info from the backend to the core program and triggers the algorithm.

        :param args: arguments
        :param kwargs: key word arguments
        :return:
        """
        if genre == 'waltz':
            self.song = Waltz(key_signature, emotion, tempo, chaos_factor) #waltz takesgpt api keytracks, key and tempo for now.
            self.song.compose()
        return 0 if self.song.song_complete else -1
    

    def get_mp3(self) -> Path:
        """
        Method to retrieve the path to the backing track in MP3 file format.
        Only works if it has been created.

        :return: path to the MP3 file
        """
        if not self.song.song_complete:
            return Path()

        return self.song.mp3File.path

    def get_midi(self) -> Path:
        """
        Method to retrieve the path to the backing track in MIDI file format.
        Only works if it has been created.

        :return: path to the MIDI file
        """
        if not self.song.song_complete:
            return Path()

        return self.song.midFile.path
