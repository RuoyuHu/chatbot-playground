import sys
from enum import Enum, unique


@unique
class TER_COL(Enum):
    """
    Terminal output colours, can be used in logging to show highlights in text
    """
    END = 0,
    BOLD = 1,
    GREEN = 2,
    YELLOW = 3,

    def __str__(self):
        if self == TER_COL.END:
            return '\033[0m'
        elif self == TER_COL.BOLD:
            return '\033[1m'
        elif self == TER_COL.GREEN:
            return '\033[92m'
        elif self == TER_COL.YELLOW:
            return '\033[93m'


def colourise(s, colour=TER_COL.BOLD):
    """
    Wrap given text in colour strings
    """
    return str(colour) + str(s) + str(TER_COL.END)


# Target output stream, defaults to stdout if None
_FPRINT_OUTPUT_FILE = None

def fprint_init(output_stream=None):
    """
    Initialise and set output stream for all fprint instances
    """
    global _FPRINT_OUTPUT_FILE
    if output_stream is not None:
        _FPRINT_OUTPUT_FILE = open(output_stream, 'w')


def fprint(*objects, sep=' ', end='\n', colour=None):
    """
    Custom wrapper for default print function to output to a unified output
    stream
    """
    if colour is not None:
        objects = tuple([colourise(item) for item in objects])
    global _FPRINT_OUTPUT_FILE
    if _FPRINT_OUTPUT_FILE is not None:
        print(*objects, sep=sep, end=end, file=_FPRINT_OUTPUT_FILE, flush=True)
    else:
        print(*objects, sep=sep, end=end)


def fprint_json(args, sep=' ', end='\n'):
    """
    fprint json objects as key, value pairs
    """
    for key in args.keys():
        fprint(f"{key}={args[key]}", sep=sep, end=end)

