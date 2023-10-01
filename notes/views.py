from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/signin/')
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
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
