from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

# Register the custom admin class for the User model
admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, CustomUserAdmin)  # Register the User model with the custom admin
