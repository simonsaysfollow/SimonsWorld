import requests
from django.http import HttpResponse
from django.shortcuts import render
import templates
import glob
import os 

mailgun_api_key = os.environ["MAILGUN_API_KEY"]

holder = []
all_html_files = glob.glob("templates/*.html")
for single in all_html_files:
    file_name = os.path.basename(single)
    name_only, extension = os.path.splitext(file_name)
    if name_only != 'base':
        holder.append(name_only)


def index(request):
    context = {
        'title': 'Simon Tekeste',
        "y": holder,
        "checker":"home"
            }
    return render(request, 'home.html', context)


def second(request):

    context = {
        "title": "Projects",
        "y": holder,
        "checker":"travel"
    }
    return render(request, "travel.html", context)

def connect_with_me(request):
    
    if request.method != "GET":
        first = request.GET["user_first"]
        last = request.GET["user_last"]
        email = request.GET["user_mail"]
        message = request.GET["user_message"]
        phone = request.GET["phone_number"]
        company = request.GET["company_name"]

    
        HttpResponse=('''<h1>this crazy</h1>''')
        return HttpResponse
    else:
        context = {
            "title": "Contact Me",
            "y": holder,
            "checker": "contact"

        }
        return render(request, "contact.html", context)
