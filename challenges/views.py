from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenge.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())

    if month > len(months):
        raise Http404()
    redirect_month = months[month - 1]
    redirect_url = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "challengeText": challenge_text
        })
    except:
        raise Http404()