from django import forms

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(label='Senha', required=True,
                            widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
