from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )

class RegistrationForm(UserCreationForm):
    password1 = forms.RegexField(label = "Password", regex = r'^[\w.@+-]+$', help_text = "Password must be six characters long and contain at least one non-alphanumberic character.", widget = forms.PasswordInput, min_length = 6, )
    password2 = forms.RegexField(label = "Password confirmation", regex = r'^[\w.@+-]+$', widget = forms.PasswordInput, min_length = 6)
    email = forms.EmailField(max_length = 50)
