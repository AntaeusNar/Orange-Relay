#  This file should only load AFTER FakeRPi.GPIO is loaded, if that one is needed.  Here we are wanted to overide some
#  functionality of the FakeRPi.GPIO to give a little bit more of an emulation.  honestly this probely needs to be
#  forked and rewritten as a separate package for dev work, but here we are.....

# The basic idea is that when a pin is made HIGH or LOW it is writen into a file,
# and then when the input is checked it reads the file.......

import json
from FakeRPi.GPIO import *




def output(channel, state):
    """
    To set the output state of a GPIO pin:
    :param channel:
    :return:
    """

    # should try to open the json file containing the pin dict with error handling options
    with open('pins.json', 'r') as (json_file, err):
        if err:
            pins = {}
        else:
            pins = json.load(json_file)

    if channel in pins:
        pins[channel] = state
    else:
        pins[channel] = state

    with open('pins.json', 'w') as json_file:
        json.dump(pins, json_file)
    json_file.close()
    print('did this run')
    return state
