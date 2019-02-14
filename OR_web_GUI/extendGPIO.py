#  This file should only load AFTER OPi.GPIO is loaded, if that one is needed.  Here we are wanted to override some
#  functionality of the OPi.GPIO to give a little bit more of an emulation.  honestly this probably needs to be
#  forked and rewritten as a separate package for dev work, but here we are.....

# The basic idea is that when a pin is made HIGH or LOW it is writen into a file,
# and then when the input is checked it reads the file.......

from . import extendJSON as JSON


def output(channel, state):
    """
    To set the output state of a GPIO pin:
    :param channel:
    :return:
    """

    # should try to open the json file containing the pin dict with error handling options
    try:
        pins = JSON.getJSONfile('pins.json')
        pins = {int(k): v for k, v in pins.items()}
    except EnvironmentError:
        pins = {}

    if channel not in pins:
        pins[channel] = state
    else:
        pins[channel] = state

    JSON.writeJSONfile('pins.json', pins)

    return state


def input(channel):
    """
    To read the value of a GPIO pin:
    :param channel:
    :return:
    """

    # Should try to open the json file containing the pin dict
    try:
        pins = JSON.getJSONfile('pins.json')
        pins = {int(k): v for k, v in pins.items()}
    except EnvironmentError:
        pins = {}

    if channel not in pins:
        return LOW
    else:
        state = pins[channel]

    return state
