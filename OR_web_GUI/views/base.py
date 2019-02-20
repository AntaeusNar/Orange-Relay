# django imports
from django.shortcuts import render
from django.template.defaulttags import register

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


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    # Usage: in template -> {{ mydict|get_item:item.NAME }}


def index(request):
    # Basic Index
    inputs = Input.objects.order_by('date_added')
    rules = Rule.objects.order_by('date_added')
    outputs = Output.objects.order_by('date_added')
    for output in outputs:
        output.state = GPIO.input(output.channel)
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
    status = {}
    # todo: fix inop code to allow for showing the status of related outputs
    for input in inputs:
        for rule in input.rule_set.all():
            status['rule.output.pk'] = GPIO.input(rule.output.channel)
    context = {'inputs': inputs, 'status': status, 'fake': fake}
    return render(request, 'OR_web_GUI/inputs.html', context)


def outputs(request):
    # Outputs index page
    outputs = Output.objects.order_by('date_added')
    for output in outputs:
        output.state = GPIO.input(output.channel)
    context = {'outputs': outputs, 'fake': fake}
    return render(request, 'OR_web_GUI/outputs.html', context)