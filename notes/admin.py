
from django.contrib import admin
from .models import Note, TrashNote


admin.site.register(TrashNote)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Customize how the Note model is displayed in the admin interface, if needed
    list_display = ['title', 'user', 'created_at']
    # Add any other admin options as necessary
