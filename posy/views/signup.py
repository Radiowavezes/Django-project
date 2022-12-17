from django.shortcuts import render
from posy.forms.user_registration import UserRegistrationForm
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login
import logging


def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        newuser = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )
        try:
            newuser.save()
            login(request, authenticate(username=username, password=password))
            return HttpResponseRedirect(reverse("index"))
        except Exception as error:
            logging(error)
            return HttpResponse("Something went wrong.")
    else:
        form = UserRegistrationForm()
    return render(request, "signup.html", {"form": form})
