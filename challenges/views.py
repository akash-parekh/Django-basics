from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += "<li><a href =\"{0}\">{1}</a></li>".format(month_path, capitalized_month)

    response_data = "<ul>{0}</ul>".format(list_items)
    return HttpResponse(response_data)

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_url = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Invalid month")