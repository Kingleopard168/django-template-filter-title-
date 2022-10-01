from calendar import month
from http.client import HTTPResponse
import imp
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string

import challenges

monthly_challenges = {
    "january":"Eat no meat for the entire month",
    "february":"walk for at least 20 minuters every day",
    "march":"Learn Django for at least 20 minutes every day",
    "april":"Eat no meat for the entire month",
    "may":"Learn Django for at least 20 minutes every day",
    "june":"at no meat for the entire month",
    "july":"Learn Django for at least 20 minutes every day",
    "august":"walk for at least 20 minuters every day",
    "september":"Eat no meat for the entire month",
    "october":"Learn Django for at least 20 minutes every day",
    "november":"walk for at least 20 minuters every day",
    "december":"Learn Django for at least 20 minutes every day"
}
# Create your views here.

def index(request):
    list_items = ""
    month = list(monthly_challenges.keys())

    for month in month:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challenges", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    

def january(request):
    return HttpResponse("Eat no meat for the entire month")

def february(request):
    return HttpResponse("walk for at least 20 minuters every day")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenges", args=[redirect_month]) #challenges/january
    return HttpResponseRedirect(redirect_path)
#    return HttpResponseRedirect("/challenge/"+ redirect_month)
#    return HttpResponse(month)
    
def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
#shot cut code
        return render(request,"challenges/challenge.html", {
            "text" : challenges_text,
            "month_name": month
            })    
#        response_data = render_to_string("challenges/challenge.html")
#        response_data =f"<h1>{challenges_text}</h1>"
#        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")

#    if month == "january":
#       challenges_text = "Eat no meat for the entire month"
#    elif month == "february":
#        challenges_text = "walk for at least 20 minuters every day"
#    elif month == "march":
#        challenges_text = "Learn Django for at least 20 minutes every day"
#    else:
#        return HttpResponseNotFound("this month is not supported")
#    return HttpResponse(challenges_text)