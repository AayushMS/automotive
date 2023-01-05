from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login

from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")
        
class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid username or password')
        self.user = user
        return cleaned_data
    
    def login_user(self):
        login(self.request, self.user)
    
    