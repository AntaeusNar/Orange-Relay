# django imports
from django.shortcuts import render

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


def index(request):
    # Basic Index
    # todo: expand to show status of outputs
    inputs = Input.objects.order_by('date_added')
    rules = Rule.objects.order_by('date_added')
    outputs = Output.objects.order_by('date_added')
    context = {'inputs': inputs, 'outputs': outputs, 'rules': rules, 'fake': fake}
    return render(request, 'OR_web_GUI/index.html', context)


def rules(request):
    """Shows the rules"""
    rules = Rule.objects.order_by('date_added')
    for rule in rules:
        rule.output.state = GPIO.input(rule.output.channel)
    context = {'rules': rules, 'fake': fake}
    return render(request, 'OR_web_GUI/rules.html', context)


def inputs(request):
    # Inputs index page
    inputs = Input.objects.order_by('date_added')
    # todo: fix inop code to allow for showing the status of related outputs
    """     - this code is inop, the adjusted state doesn't get passed on
    for input in inputs:
        print(input)
        for rule in input.rule_set.all():
            print(rule)
            rule.output.state = GPIO.input(rule.output.channel)
            print(rule.output.state)
    """
    context = {'inputs': inputs, 'fake': fake}
    return render(request, 'OR_web_GUI/inputs.html', context)


def outputs(request):
    # Outputs index page
    outputs = Output.objects.order_by('date_added')
    for output in outputs:
        output.state = GPIO.input(output.channel)
    context = {'outputs': outputs, 'fake': fake}
    return render(request, 'OR_web_GUI/outputs.html', context)