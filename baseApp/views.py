from typing import List, Dict
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Doctor, Review
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
'''
homepage view =============================================================================
'''


def home(request: HttpRequest) -> HttpResponse:
    """
    Renders the home page with doctors and reviews based on user input.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object that renders the home page.
    """
    # Retrieve all doctors and reviews from the database
    doctors = Doctor.objects.all()
    rating = Review.objects.all()

    # Get search parameters from the request's GET parameters
    spec = request.GET.get('specification')
    loc = request.GET.get('address')

    # Filter doctors based on user input
    if spec and loc:
        doctors_in_my_location = doctors.filter(
            Q(specialization__icontains=spec) & Q(address__icontains=loc)
        )
    else:
        doctors_in_my_location = []

    # Create context dictionary
    context: Dict[str, any] = {
        'doctors': doctors,
        'rating': rating,
        'locDoctors': doctors_in_my_location,
        'search_pressed': bool(spec and loc),
    }

    # Add message if doctors_in_my_location is empty
    if not doctors_in_my_location:
        context['message'] = 'No results found'

    return render(request, "baseApp/index.html", context)


def createUser(request):
    """
    Create a new user and authenticate them.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.

    Raises:
        None
    """
    if request.method == "POST":
        # Get user data from request
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create user
        user = User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email,
            password=password
        )

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            # Login user and redirect to home page
            login(request, user)
            return redirect('home')
        else:
            print("Authentication failed")
    else:
        print("Could not create a user")

    # Render login-register.html template
    return render(request, "baseApp/login-register.html")

   
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
#doctor view
def doctorView(request):
    return render(request, "baseApp/doctorview.html")