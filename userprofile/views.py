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
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


def custom_logout(request):
    logout(request)
    return redirect('userprofile:signin')


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

            pass

    return render(request, 'userprofile/sign_in.html')


from django.core.exceptions import ValidationError
import logging

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('note_list')  # Redirect to the desired page after signup
            except Exception as e:
                logging.error(e)  # Log any exceptions that occur
                # You can also print e to the console for debugging purposes
        else:
            print(form.errors)  # Print form errors to the console for debugging

    else:
        form = UserCreationForm()

    return render(request, 'userprofile/sign_up.html', {'form': form})