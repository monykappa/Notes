# notesapp/admin.py
from django.contrib import admin
from .models import Signup, Note

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    # Customize how the Signup model is displayed in the admin interface, if needed
    list_display = ['user', 'id']
    # Add any other admin options as necessary

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Customize how the Note model is displayed in the admin interface, if needed
    list_display = ['title', 'user', 'created_at']
    # Add any other admin options as necessary
