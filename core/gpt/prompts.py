from typing import Dict, Any

from core.gpt.constants import NO_DES


class Prompt:

    def __init__(self):
        self.prompt = ""

    def __call__(self, *args, **kwargs):
        return self.prompt + NO_DES


class PromptManager:

    prompts: dict[str, Prompt]

    def __init__(self):
        self.prompts = {}

    def get_prompt_by_name(self, name):
        return self.prompts[name]()
