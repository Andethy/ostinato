import os

from core.gpt.prompts import *
import openai


class Responder:

    def __init__(self, prompter: PromptManager, key):
        self.prompter = prompter
        self.__key = os.getenv('GPT_API_KEY') if key is None else key

    def get_response(self, prompt_type=0):
        self.prompter.get_prompt_by_name()
        return None
