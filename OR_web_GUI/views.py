from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers


from .models import Rule, Input, Output
from .forms import OutputForm, RulesForm, InputForm, LinkingLogicForm


"""In order to get around not have select.epoll in a windows environment we are implementing
FakeRPi.GPIO which emulates the existence of the GPIO"""
try:
    import OPi.GPIO as GPIO
    fake = False
except ImportError:
    from .packages import extendGPIO as GPIO
    fake = True
    print('The linux_interaction() function was not executed')


# Create your views here.

# base views


def index(request):
    """The home page for OR_web_GUI"""
    inputs = Input.objects.exclude(rule__text=None)
    outputs = Output.objects.exclude(rule__text=None)
    context = {'inputs': inputs, 'outputs': outputs, 'fake': fake}
    return render(request, 'OR_web_GUI/index.html', context)


def rules(request):
    """Shows the rules"""
    rules = Rule.objects.order_by('date_added')
    for rule in rules:
        rule.output.state = GPIO.input(rule.output.channel)
    context = {'rules': rules, 'fake': fake}
    return render(request, 'OR_web_GUI/rules.html', context)


def inputs(request):
    """shows the inputs"""
    inputs = Input.objects.order_by('date_added')
    for input in inputs:
        print(input)
        for rule in input.rule_set.all():
            print(rule)
            rule.output.state = GPIO.input(rule.output.channel)
            print(rule.output.state)
    context = {'inputs': inputs, 'fake': fake}
    return render(request, 'OR_web_GUI/inputs.html', context)


def outputs(request):
    """shows those outputs"""
    outputs = Output.objects.order_by('date_added')
    for output in outputs:
        output.state = GPIO.input(output.channel)
    context = {'outputs': outputs, 'fake': fake}
    return render(request, 'OR_web_GUI/outputs.html', context)

# Configuration views
# todo: look at refactoring the new_****** functions to allow for a single function to handle all new_******


def new_output(request):
    """adds new output"""
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = OutputForm()
    else:
        # POST data submitted; process data.
        form = OutputForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('OR_web_GUI:outputs'))
    context = {'form': form}
    return render(request, 'OR_web_GUI/new_output.html', context)


def new_rule(request):
    """adds new rules"""
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = RulesForm(initial={'action': 'T', 'times': 'P'})
    else:
        # POST data submitted; process data.
        form = RulesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('OR_web_GUI:rules'))
    context = {'form': form, 'fake': fake}
    return render(request, 'OR_web_GUI/new_rule.html', context)


def new_input(request):
    """adds new inputs"""
    if request.method != 'POST':
        form = InputForm()
    else:
        form = InputForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('OR_web_GUI:inputs'))
    context = {'form' : form, 'fake': fake}
    return render(request, 'OR_web_GUI/new_input.html', context)

#  action views: basically there is no real reason hitting a url NEEDS to return a web page, that just what we do when
#  we let people use it, but we can have the 'view' do other things, like activate gpio pins


def state_toggle(request, whichmodel, key_id):
    if whichmodel == 'Output':
        relay_control(key_id)
    elif whichmodel == 'Input':
        # todo: add state changes based on rules or inputs
        fish
    elif whichmodel == 'Rule':
        follow_the_rules(key_id)
        """should return back to previous page"""
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def relay_state(request, output_id):
    """will grab the output sent to it and return the state of said output"""
    output = Output.objects.get(id=output_id)
    state = GPIO.input(output.channel)
    if state:
        return render(request, 'OR_web_GUI/outputStateGreen.html')
    elif not state:
        return render(request, 'OR_web_GUI/outputStateRed.html')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# additional functions......

def follow_the_rules(rule_id):
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
    # todo: fix this mess.....
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


# ajax views
