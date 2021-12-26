from django.urls import path
from . import views

# This is the file where you can tell Django which views to respond to a request with when a certain url is hit.
# You do this by creating a list of the urls that you want to support. Import path from django.urls.

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]