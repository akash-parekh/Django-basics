from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "This Works!"
    elif month == "februray":
        challenge_text = "Walk Walk Wak"
    elif month == "march":
        challenge_text = "Complete this course by weekend"
    else:
        return HttpResponseNotFound("This month is not supported yet!")
    return HttpResponse(challenge_text)