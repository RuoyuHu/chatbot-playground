## Utils

This directory contains utility functions for the chatbot playground

`fprint.py` Logging functions, prints output to either `stdout` or a specified output file. Necessary for logging use in the gpu cluster.

`loaders.py` Loader function custom to each model type. Accessed through the `load_model_for_generation` endpoint.