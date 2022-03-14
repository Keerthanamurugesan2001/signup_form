from django.shortcuts import render
from django.http import HttpResponse
from .form import CreateNewSignForm
from .models import SignDetails


# Create your views here.
def index(response):
    if response.method == "POST":
        form = CreateNewSignForm()

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            t = SignDetails(username=username, password=password)
            t.save()

    return render(response, 'signup/signup.html', {"form": form})
