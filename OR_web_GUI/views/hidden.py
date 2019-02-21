"""Normal functions we want loaded with the views"""

# local imports
from OR_web_GUI.models import Rule, Input, Output

# import for GPIO in real vs. test env
try:
    import OPi.GPIO as GPIO

    fake = False
except ImportError:
    from OR_web_GUI.packages import extendGPIO as GPIO

    fake = True
    print('The linux_interaction() function was not executed')


def follow_the_rules(rule_id):
    # todo: rebuild to allow for logic
    # todo: rebuild to allow for timed control
    # should be given a rule follow the logic and then trigger the correct relay(s)
    rule = Rule.objects.get(id=rule_id)
    if rule.action == 'H':
        # set output high
        key_id = rule.output.pk
        relay_control(key_id, 'high')
    elif rule.action == 'L':
        # set output low
        key_id = rule.output.pk
        relay_control(key_id, 'low')
    elif rule.action == 'T':
        # toggle output
        key_id = rule.output.pk
        relay_control(key_id, 'toggle')


def relay_control(key_id, state='toggle'):
    # takes a relay and sets it to the requested state
    output = Output.objects.get(id=key_id)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(output.channel, GPIO.OUT)
    if state == 'toggle':
        GPIO.output(output.channel, not GPIO.input(output.channel))
    elif state == 'high':
        GPIO.output(output.channel, GPIO.HIGH)
    elif state == 'low':
        GPIO.output(output.channel, GPIO.LOW)


def check_status(key_id, whichmodel):
    # todo: rebuild to be single point of status checking
    # todo: build new function to allow for ajax calls
    # takes a key_id and model type and gets the status (high/true or low/false) of related outputs returned as a dic
    # dic = {
    #   rules:
    statuses = {}
    if whichmodel == 'Input':
        input = Input.objects.get(id=key_id)
        for rule in input.rule_set.all():
            statuses[rule.pk] = {}
            for output in rule.outputs:
                pass
    elif whichmodel == 'Rule':
        pass
    elif whichmodel == 'Output':
        pass


def check_output_state(key_id):
    # is given an output id and checks the state of the output, then returns the output object with the state
    output = Output.objects.get(id=key_id)
    state = GPIO.input(output.channel)
    return state
