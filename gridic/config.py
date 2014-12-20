import os

PROJECT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
STATIC_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'static')

SOUNDFONT_FILE = "/DB/soundfonts/mysoundfont.sf2"
MIDI_KEY_MAPPING = {
    0: 93,
    1: 91,
    2: 89,
    3: 86,
    4: 83,
    5: 81,
    6: 78,
    7: 76,
    8: 74,
    9: 71,
    10: 69,
    11: 66,
    12: 64,
    13: 62,
    14: 59,
    15: 57
}

HOST = 'localhost'
PORT = 9910