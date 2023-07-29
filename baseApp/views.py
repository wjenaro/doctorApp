from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Doctor, Review
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

def home(request):
    doctors=Doctor.objects.all()
    rating=Review.objects.all()
    # Get the search parameters from the form
    specification = request.GET.get('specification')
    address = request.GET.get('address')
    # Create a queryset of doctors that match the search parameters
    doctors_search = Doctor.objects.filter(
        specialization__icontains=specification,
        address__icontains=address
    )
    ratings = []
    for doctor in doctors_search:
        rating1 = 0
        reviews = Review.objects.filter(doctor=doctor)
        if reviews.count() > 0:
            rating1 = sum(review.rating for review in reviews) / reviews.count()
        ratings.append((doctor, rating1))


    context={'doctors': doctors, 'rating':rating, 'doct':ratings}
   
    return render(request, "baseApp/index.html", context)
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
            messages.add_message(request, messages.INFO, "Hello world.")
            print ("Data not sent")

    return render(request, "baseApp/login-register.html", {"form": form})
#login
@csrf_protect
@ensure_csrf_cookie
def loginUser(request):
    #let login
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('home')
        else: #if user is not fould, then a message 
            print('User not found')      
 

    context={}
    return render(request, "baseApp/login.html", context)
def logoutView(request):
    logout(request)
    return redirect('home')