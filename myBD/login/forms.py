from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from models import Administrador, Marketing, Cliente

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[
        ('Administrador', 'Administrador'),
        ('Marketing', 'Marketing'),
        ('Cliente', 'Cliente'),
    ])

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user_type = self.cleaned_data['user_type']
        user = User.objects.create_user(username=username, password=password)

        if user_type == 'Administrador':
            Administrador.objects.create(user=user)
        elif user_type == 'Marketing':
            Marketing.objects.create(user=user)
        elif user_type == 'Cliente':
            Cliente.objects.create(user=user)

        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Credenciales inválidas")
        self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user
