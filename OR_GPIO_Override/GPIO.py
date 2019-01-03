#  This file should only load AFTER FakeRPi.GPIO is loaded, if that one is needed.  Here we are wanted to overide some
#  functionality of the FakeRPi.GPIO to give a little bit more of an emulation.  honestly this probely needs to be
#  forked and rewriten as a seperate package for dev work, but here we are.....

# The basic idea is that when a pin is made HIGH or LOW it is writen into a file, and then when the input is checked it reads the file.......

import json


def output(channel, state):
    """
    To set the output state of a GPIO pin:
    :param channel:
    :return:
    """
    try:
        with open('pins.json') as json_file:
            pins = json.load(json_file)
    finally:
        pins = {}
        pins

    return LOW