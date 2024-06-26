from django import forms

class CreateDbForm(forms.Form):
    nome = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome do esquema'}))