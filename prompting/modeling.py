import os
import torch

from prompting.prompt_loader import PromptLoader
from utils.loaders import load_model_for_generation


def load_prompter(**kwargs):
    """
    Loads and returns a prompter object to speedd up experiment setup
    """
    model, tokenizer, pipeline = load_model_for_generation(**kwargs)
    prompter = PromptLoader(tar="prompting/prompt.txt", pipeline=pipeline)
    return prompter