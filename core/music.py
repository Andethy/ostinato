from core.gpt.prompts import *
from core.gpt.responses import Responder
from core.midi.score import Score


class Song:

    def __init__(self, key, tempo, chaos):
        self.tempo = tempo
        self.key = key
        self.chaos = chaos
        self.score = Score()
        self.prompts = PromptManager()
        self.responder = Responder(self.prompts)

    def compose_track(self, track_name):
        pass

    def write_ostinato(self):
        pass


class Waltz(Song):

    def __init__(self, key, tempo, *args, **kwargs):
        super().__init__(key, tempo, 0.5)

    def compose_track(self, track_name):
        pass

    def write_ostinato(self):
        pass

    def create_section(self):
        pass
