# django imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# local imports
from OR_web_GUI.forms import OutputForm, RulesForm, InputForm


def new_rule(request):
    # Add additional rules
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
    # Add additional inputs
    if request.method != 'POST':
        form = InputForm()
    else:
        form = InputForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('OR_web_GUI:inputs'))
    context = {'form' : form, 'fake': fake}
    return render(request, 'OR_web_GUI/new_input.html', context)


def new_output(request):
    # Add additional outputs
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