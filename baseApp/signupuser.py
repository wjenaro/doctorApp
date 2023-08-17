from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
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