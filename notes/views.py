from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        # Handle form submission
        form = NoteForm(request.POST, instance=note)  # Use your form if available
        if form.is_valid():
            form.save()
            # Redirect to the note list page
            return redirect('note_list')

    return render(request, 'notes/note_detail.html', {'note': note})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def custom_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after signup
            login(request, user)
            return redirect('note_list')  # Redirect to the notes page after signup
    else:
        form = UserCreationForm()
    return render(request, 'userprofile/signup.html', {'form': form})   