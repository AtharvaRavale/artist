from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Artist  # Import both models together

class UserRegisterForm(UserCreationForm):
    """User registration form"""
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # Use the custom user model
        fields = ['username', 'email', 'password1', 'password2']

class ArtistForm(forms.ModelForm):
    """Form to add an artist (admin only)"""
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'expertise', 'image']
