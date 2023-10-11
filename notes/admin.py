
from django.contrib import admin
from .models import Note, Trash


@admin.register(Trash)
class TrashAdmin(admin.ModelAdmin):
    list_display = ('user', 'note', 'deleted_at')
    list_filter = ('user', 'deleted_at')
    search_fields = ('user__username', 'note__title')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Customize how the Note model is displayed in the admin interface, if needed
    list_display = ['title', 'user', 'created_at']
    # Add any other admin options as necessary
