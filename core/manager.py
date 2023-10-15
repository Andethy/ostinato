from pathlib import Path
from core.music import Waltz

class CoreManager:

    def __init__(self):
        self.song = None

    def pass_request(self, *args, **kwargs) -> int:
        """
        Passes in form info from the backend to the core program and triggers the algorithm.

        :param args: arguments
        :param kwargs: key word arguments
        :return:
        """
        kwargs['genre'] = 'waltz'
        if kwargs['genre'] == 'waltz':
            self.song = Waltz(*args)
        return 0

    def get_mp3(self) -> Path:
        """
        Method to retrieve the path to the backing track in MP3 file format.
        Only works if it has been created.

        :return: path to the MP3 file
        """
        if not self.song.song_complete:
            return Path()

        return Path()

    def get_midi(self) -> Path:
        """
        Method to retrieve the path to the backing track in MIDI file format.
        Only works if it has been created.

        :return: path to the MIDI file
        """
        if not self.song.song_complete:
            return Path()

        return Path()

