## Prompting

This directory contains files used to perform single inference experiments. Can be used to familiarise with the process of prompting generative transformer models.

`config.json` Generation config

`modeling.py` Contains load functions for the prompter object

`prompt_loader` Contains the PromptLoader object used for single inference

`prompt.txt` Prompt contained in a text file, can be changed while the python instance is active


## Quick Start

A example for running single inference on using the prompt loader

```
cd chatbot-playground
python3
```

Within the python instance

```
from prompting.modeling import load_prompter
prompter = load_prompter(model_type='opt-2.7b')
prompter.run_prompt()
```

The generated text will be shown in the terminal, the full output including the initial prompt is in `output.log`

```
cat output.log
```