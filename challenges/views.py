from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenge = {
    "january": "This Works!",
    "febuary": "Walk Walk Walk",
    "march": "Complete this course by weekend",
    "april": "This Works!",
    "may": "Walk Walk Walk",
    "june": "Complete this course by weekend",
    "july": "This Works!",
    "august": "Walk Walk Walk",
    "september": "Complete this course by weekend",
    "october": "This Works!",
    "november": "Walk Walk Walk",
    "december": "Complete this course by weekend"
}

# Create your views here.

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Invalid month")