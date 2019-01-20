import requests
from django.http import HttpResponse
from django.shortcuts import render
import templates
import glob
import os 


def index(request):
    context = {
        'title': 'Simon Tekeste',

            }
    return render(request, 'home.html', context)

def about(request):
    context = {
        "tilte": "About Me",
        
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        "title":"Contact"
    }
    return render(request, 'contact.html', context)