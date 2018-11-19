from django.shortcuts import render

# Create your views here.


def index(request):
    """The home page for OR_web_GUI"""
    return render(request, 'OR_web_GUI/index.html')
