from core.gpt.constants import *
from core.midi.constants import get_key_notes, TONICS_STR


class Prompt:
    prompt: list[str]

    def __init__(self, *args, **kwargs):
        self.prompt = []
        self.explanatory = kwargs.get('explanatory', False)
        self.create_prompt(*args)

    def __call__(self, *args, **kwargs):
        return '. '.join(self.prompt + [NO_DESC])

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
        self.num_notes = num_notes
        self.valid_characters = tuple(TONICS_STR.keys()) + (STANDARD_REST,)

    def create_prompt(self, tonic, emotion, num_notes):
        self.prompt.append(f'Generate 1 musical ostinato for a WALTZ in the key {tonic} {EMOTION_PARSER[emotion]} '
                           f'(available notes are {get_key_notes(tonic, EMOTION_PARSER[emotion])})')
        self.prompt.append(f'This ostinato will be in the format: "{STANDARD_FORMAT}"')
        self.prompt.append(f'Separate each note with "{SEPERATOR}"')
        self.prompt.append(f'Do not include dashes and in place of a note put a "{STANDARD_REST}" if there is a rest')
        self.prompt.append(f'Each note is the length of a 1/8th note')
        self.prompt.append(f'Create a total of EXACTLY {num_notes} [note]s')

    def parse_result(self, result: str):
        # result = result.replace(' ', '').replace('\n', '').replace('"', '')
        chars_to_remove = ' \n"{}'
        trans_table = str.maketrans("", "", chars_to_remove)
        result = result.translate(trans_table)
        start = 0
        for index, char in enumerate(result):
            if char in self.valid_characters and (result[index + 1] == SEPERATOR or result[index + 2] == SEPERATOR):
                end = start
                bars = 0
                for n in range(index + 1, len(result)):
                    if result[n] == SEPERATOR:
                        bars += 1
                        if bars >= self.num_notes - 1:
                            end -= 1
                            break
                    elif result[n] not in self.valid_characters:
                        end -= 1
                        break
                    end += 1
                break
            start += 1
        end = len(result)
        # for index, char in enumerate(result[::-1]):
        #     if char in self.valid_characters and (result[index - 1] == SEPERATOR or result[index - 2] == SEPERATOR):
        #         break
        #     end -= 1
        return result[start:end]


class PromptManager:
    prompts: dict[str, Prompt]

    def __init__(self):
        self.prompts = {}

    def get_prompt_by_name(self, name: str):
        return self.prompts[name]()

    def parse_prompt_by_name(self, name: str, result: str):
        return self.prompts[name].parse_result(result)


if __name__ == '__main__':
    p1 = OstinatoPrompt('F', 'sad', 6)
