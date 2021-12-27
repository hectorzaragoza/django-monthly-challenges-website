from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

# These were hardcoded route/response...monthly_challenge implements dynamic req/res
# def january(request):
#     return HttpResponse("Eat no meat for the entire month!") 

# def february(request):
#     return HttpResponse("Run 30 miles a week!")

# def march(request):
#     return HttpResponse("Job Hunt for 2 hours a day!")

# You can create if else statements to check for different url patterns but it's more efficient
# challenge_text = None
#     if month == 'january':
#         challenge_text = "Eat no meat for the entire month!"
#     elif month == 'february':
#         challenge_text = "Run 30 miles a week!"
#     elif month == 'march':
#         challenge_text = "Job Hunt for 2 hours a day!"
#     else:
#         return HttpResponseNotFound("This month is not supported!")
# to create a dictionary to check against

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Run 30 miles a week!",
    "march": "Job Hunt for 2 hours a day!",
    "april": "Run 35 miles a week!",
    "may": "Run 45 miles a week!",
    "june": "Run 50 miles a week!",
    "july": "Run 55 miles a week!",
    "august": "Run 60 miles a week!",
    "september": "Run 65 miles a week!",
    "october": "Run 70 miles a week!",
    "november": "Run 75 miles a week!",
    "december": "Run 80 miles a week!"
}

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month.")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # This line replaces the render_to_string line and the HttpResponse
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")



