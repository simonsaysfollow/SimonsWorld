import requests
from django.http import HttpResponse
from django.shortcuts import render
import templates
import glob
import os 


def index(request):
    context = {
        'title': 'Simon Tekeste',
        "checker":"home",
            }
    return render(request, 'home.html', context)

def about(request):
    context = {
        "tilte": "About Me",
        "checker":"about",
    }
    return render(request, 'about.html', context)