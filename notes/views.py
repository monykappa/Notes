from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from django.db.models import F


    

def user_profile_view(request):
    # Get the user's profile based on the currently logged-in user
    user_profile = UserProfile.objects.get(user=request.user)

    return render(request, 'notes/profile.html', {'user_profile': user_profile})

@login_required(login_url='/signin/')
def note_list(request):
    # Filter notes to show only the ones associated with the logged-in user
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required(login_url='/signin/')
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Create a new note associated with the logged-in user
            note = form.save(commit=False)  # Don't save the form just yet
            note.user = request.user  # Set the user for the note
            note.save()  # Now save the note with the user information
            return redirect('note_list')
    else:
        form = NoteForm()

    # Check if the form data is not empty and save it
    if request.method == 'GET' and any(request.GET.get(field) for field in ['title', 'content']):
        form = NoteForm(request.GET)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')

    return render(request, 'notes/note_form.html', {'form': form})



@login_required
def note_detail(request, note_id):
    # Get the main note
    note = get_object_or_404(Note, id=note_id)

    # Retrieve the latest notes for the current user (excluding the current note)
    latest_notes = Note.objects.filter(user=request.user).exclude(id=note_id).order_by('-created_at')[:5]

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')

    return render(request, 'notes/note_detail.html', {'note': note, 'latest_notes': latest_notes})


