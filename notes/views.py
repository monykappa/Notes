from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile


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
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
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
