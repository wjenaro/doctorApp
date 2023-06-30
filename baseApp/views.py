from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, "baseApp/index.html")
#creating user
def createUser(request):
    form=SignUpForm()
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user= authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print ("Data not sent")

    return render(request, "baseApp/login-register.html", {"form": form})
#login
def loginUser(request):
    form = AuthenticationForm()
    context={"form":form}
    return render(request, "baseApp/login.html", context)