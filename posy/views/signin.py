from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from posy.forms.user import UserForm
from django.http import HttpResponse


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse("Користувач з такими даними відсутній")

        login(request, user)
        return redirect("/")

    else:
        form = UserForm()
        return render(request, "login.html", {"form": form})
