from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as lazy
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'username': lazy('Pseudo'),
        }


class UsernameUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username']
        labels = {
            'username': lazy(''),
        }
        help_texts = {
            'username': lazy(''),
        }

class EmailUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [ 'email' ]
        labels = {
            'email': lazy(''),
        }

class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'image']
        labels = {
            'image': lazy(''),
        }

class BirthdateUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthdate']
        labels = {
            'birthdate': lazy(''),
        }

class BioUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
        labels = {
            'bio': lazy(''),
        }

class External_linkUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['external_link']
        labels = {
            'external_link': lazy(''),
        }

class Facebook_linkUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['facebook_link']
        labels = {
            'facebook_link': lazy(''),
        }
