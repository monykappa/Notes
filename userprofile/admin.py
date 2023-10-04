# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html

from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_profile_picture')

    def user_profile_picture(self, obj):
        # Custom method to display the profile picture in the admin
        if hasattr(obj, 'userprofile') and obj.userprofile.profile_picture:
            return format_html('<img src="{}" width="100" height="100" />', obj.userprofile.profile_picture.url)
        else:
            return 'No profile picture'

    user_profile_picture.short_description = 'Profile Picture'

# Register the custom admin class for the User model
admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, CustomUserAdmin)  # Register the User model with the custom admin