from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from .forms import NoteForm
from .models import Trash
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from django.db.models import F



def restore_note(request):
    # Retrieve deleted notes from the Trash model for the logged-in user
    deleted_notes = Trash.objects.filter(user=request.user)
    return render(request, 'notes/trash.html', {'deleted_notes': deleted_notes})


def delete_note(request, note_id):
    # Get the note to be deleted
    note = Note.objects.get(id=note_id)

    # Create a new Trash object with the same content
    trash_note = Trash(user=request.user, note=note)
    trash_note.save()

    # Delete the original note
    note.delete()

    # Redirect to the appropriate page (note_list or trash_page)
    return redirect('note_list')  # Or 'trash_page' if you have one







    


    return render(request, 'notes/profile.html', {'user_profile': user_profile})

@login_required(login_url='/signin/')
def note_list(request):
    # Filter notes to show only the ones associated with the logged-in user
    notes = Note.objects.filter(user=request.user).order_by('-created_at')  # Order by created_at in descending order
    return render(request, 'notes/note_list.html', {'notes': notes})



def user_profile_view(request):
    # Get the user's profile based on the currently logged-in user
    user_profile = UserProfile.objects.get(user=request.user)


@login_required(login_url='/signin/')
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Create a new note associated with the logged-in user
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')

    form = NoteForm()

    return render(request, 'notes/new_note.html', {'form': form})




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


