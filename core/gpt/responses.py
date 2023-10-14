from core.gpt.prompts import *


class Responder:

    def __init__(self, prompter: PromptManager):
        self.prompter = prompter

    def get_response(self, prompt_type=0):
        return None

