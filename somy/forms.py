from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()  

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['name', 'email', 'username', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'bio', 'avatar']  # Include fields you want to edit
