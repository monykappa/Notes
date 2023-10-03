from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User 
from django.contrib.auth import logout
from .models import *
from .models import UserProfile  # Import your UserProfile model




def signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        pfp = request.FILES.get('pfp')  # Get the profile picture file if provided

        # Split the full name into first name and last name
        first_name, last_name = full_name.split(' ', 1) if ' ' in full_name else (full_name, '')

        # Check if the passwords match
        if password1 != password2:
            error_message = "Passwords do not match."
        else:
            # Check if a user with the same username or email already exists
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                error_message = "A user with this username or email already exists."
            else:
                # Create the user if the username and email are unique
                user = User(username=username, email=email, password=password1)
                user.first_name = first_name
                user.last_name = last_name

                if pfp:
                    user.profile_picture = pfp  # Save the profile picture to the User model

                user.backend = 'django.contrib.auth.backends.ModelBackend'  # Set the authentication backend
                user.save()

                # Create a UserProfile instance and link it to the user
                UserProfile.objects.create(user=user, profile_picture=pfp)

                # Log in the user
                login(request, user)
                return redirect('note_list')  # Redirect to your home page
    else:
        error_message = ""

    return render(request, 'userprofile/sign_up.html', {'error_message': error_message})





def custom_logout(request):
    logout(request)
    return redirect('userprofile:signin')


from django.contrib.auth import authenticate, login

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or protected view
            return redirect('note_list')
        else:
            # Handle authentication failure
            error_message = "Invalid username or password. Please try again."
    else:
        error_message = ""

    return render(request, 'userprofile/sign_in.html', {'error_message': error_message})
