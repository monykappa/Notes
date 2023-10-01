from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Define an inline admin class for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile

# Customize the UserAdmin class to include the UserProfileInline
class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]

# Register the User model with the CustomUserAdmin class
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register the UserProfile model separately if needed
admin.site.register(UserProfile)
