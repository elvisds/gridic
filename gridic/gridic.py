#!/usr/bin/env python

import bottle
from mingus.midi import fluidsynth

import config

@bottle.route('/play')
def play():
    requested_keys = bottle.request.query.notes.split(",")
    for key in requested_keys:
        if unicode.isdigit(key):
            midi_key = config.MIDI_KEY_MAPPING[int(key)]
            fluidsynth.play_Note(midi_key)

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, 
            root=config.STATIC_DIRECTORY)

@bottle.route('/')
def index():
    return bottle.static_file('index.html', 
            root=config.PROJECT_DIRECTORY)

def load_config(**config_params):
    for key,value in config_params.iteritems():
        setattr(config, key, value)

def run(**config_params):
    load_config(**config_params)
    fluidsynth.init(config.SOUNDFONT_FILE)
    bottle.run(host=config.HOST, port=config.PORT)

if __name__=="__main__":
    run()