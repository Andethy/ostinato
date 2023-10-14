from core.gpt.constants import *
from core.midi.constants import get_key_notes


class Prompt:

    prompt: list[str]

    def __init__(self, *args, **kwargs):
        self.prompt = []
        self.explanatory = kwargs.get('explanatory', False)
        self.create_prompt(*args)

    def __call__(self, *args, **kwargs):
        return '. '.join(self.prompt + [NO_DESC] if self.explanatory else [])

    def create_prompt(self, *args, **kwargs):
        """
        OVERRIDE THIS METHOD.

        This should construct a prompt configured by the .

        :param args:
        :param kwargs:
        """
        pass

    def parse_result(self, result: str):
        """
        OVERRIDE THIS METHOD.

        This should parse the result of the GPT response.

        :param result: parsed list of notes
        """
        pass


class OstinatoPrompt(Prompt):

    def __init__(self, tonic, emotion, num_notes):
        super().__init__(tonic, emotion, num_notes)

    def create_prompt(self, tonic, emotion, num_notes):
        self.prompt.append(f'Make an ostinato in the key {tonic} {EMOTION_PARSER[emotion]} '
                           f'(available notes are {get_key_notes(tonic, EMOTION_PARSER[emotion])})')

class PromptManager:

    prompts: dict[str, Prompt]

    def __init__(self):
        self.prompts = {}

    def get_prompt_by_name(self, name: str):
        return self.prompts[name]()

    def parse_prompt_by_name(self, name: str, result: str):
        return self.prompts[name].parse_result(result)


if __name__ == '__main__':
    p1 = OstinatoPrompt('abc')