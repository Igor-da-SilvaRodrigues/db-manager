from django import forms
from app_auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    host = forms.CharField(required=True, initial="localhost", widget=forms.TextInput(attrs={'placeholder': 'Enter host address', 'id':'hostInput'}))
    port = forms.CharField(required=True, initial="3306", widget=forms.TextInput(attrs={'id':'portInput', 'pattern': '[0-9]*', 'inputmode': 'numeric'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    