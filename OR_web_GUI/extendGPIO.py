# This file will load only if OPi.GPIO fails because of a Dev environment.

# The basic idea is that when a pin is made HIGH or LOW it is writen into a file,
# and then when the input is checked it reads the file.......

from . import extendJSON as JSON

# Values
LOW = 0
HIGH = 1

# Modes
BCM = 11
BOARD = 10

# Pull
PUD_OFF = 20
PUD_DOWN = 21
PUD_UP = 22

# Edges
RISING = 31
FALLING = 32
BOTH = 33

# Functions
OUT = 0
IN = 1
SERIAL = 40
SPI = 41
I2C = 42
HARD_PWM = 43
UNKNOWN = -1

def setwarnings( a): pass


def setmode(a): pass


def getmode(): return BCM


def setup(channel, state, initial=0, pull_up_down=None): pass

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


def cleanup(a=None): pass


def wait_for_edge(channel, edge): pass


def add_event_detect(channel, edge, callback=None, bouncetime=None): pass


def add_event_callback(channel, callback=None): pass


def remove_event_detect(channel): pass


def event_detected(channel): return False


def gpio_function(channel): return OUT