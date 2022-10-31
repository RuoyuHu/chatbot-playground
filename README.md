# Chabot playground

This folder contains the code for loading and playing with a pretrained language model as a chatbot. Developed to improve personal understanding of pre-trained language models in a conversational agent seting. For educational and research use only.

***

## Project Structure

```
chatbot-playground
├── chatbot
│   ├── README.md
│   ├── __init__.py
│   ├── chatbot.py
│   ├── config.json
│   └── prompt.txt
├── prompting
│   ├── README.md
│   ├── __init__.py
│   ├── config.json
│   ├── modeling.py
│   └── prompt.txt
│   ├── prompt_loader.py
├── utils
│   ├── README.md
│   ├── __init__.py
│   ├── fprint.py
│   └── loaders.py
├── README.md
└── run_chatbot.py
```

## Downloading Pretrained Models

This chatbot playground requires a pretrained generative language model to operate. You can find these on platforms such as [Huggingface](https://huggingface.co/docs/transformers/index). The framework originally uses an OPT [model](https://huggingface.co/facebook/opt-2.7b)

Example

```
cd chatbot-playground
git clone https://huggingface.co/facebook/opt-2.7b
```

To run the chatbot using different models, please add a new model loader function to `utils/loaders.py`, and update the model type in `chatbot/config.json`


## Quick start

You can run the chatbot instance from the `run_chatbot.py` file

```
python3 run_chatbot.py
```

## Additional Information

The `chatbot/` directory contains the source code and configuration files for loading and running the chatbot.

The `prompting/` directory contains the code and instructions for loading a model and generating responses from a single prompt.

The `utils/`  directory contains utility functions for loading models and logging.

More details are contained in the respective directories.

For questions, queries, issues, please contact ruoyu.hu18@imperial.ac.uk