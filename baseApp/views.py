from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Doctor, Review
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
'''
homepage view =============================================================================
'''
def home(request):
    doctors=Doctor.objects.all()
    rating=Review.objects.all()
    '''
    search parameters
    '''
    spec=request.GET.get('specification')
    loc=request.GET.get('address')
    '''make a search based'''
    doctors_in_my_location=[]
    search_pressed = request.GET.get('search')
    if request.GET:
        doctors_in_my_location=Doctor.objects.filter(
            specialization__icontains=spec,
            address__icontains=loc
            )
        print(type(search_pressed))
        print("These are search results :"+str(doctors_in_my_location))

    context={'doctors': doctors, 'rating':rating, 'locDoctors':doctors_in_my_location, 'search_pressed': search_pressed,}
# Check if the doctors_in_my_location list is empty
    if not doctors_in_my_location:
        context['message'] = 'No results found'


   
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