# app/users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Get CustomUserCreationForm, CustomUserChangeForm from the users app
from app.users.forms import CustomUserCreationForm, CustomUserChangeForm

# Define CustomUser from get_user_model method
CustomUser = get_user_model()

# CustomUserAdmin class
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

# Register CustomUser
admin.site.register(CustomUser, CustomUserAdmin)