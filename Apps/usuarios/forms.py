from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Ingresa tu usuario', min_length=5, required=True, widget=forms.TextInput(attrs={'placeholder':'Ingresa tu usuario', 'class':'form-control'}))
    password = forms.CharField(max_length=50, label='Ingresa tu contraseña', min_length=5, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Ingresa tu contraseña','class':'form-control'}))

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email', 'first_name', 'last_name']
        widgets={
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa el usuario deseado.'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese una contraseña '}),
            'email' : forms.TextInput(attrs={'class':'form-control',
            'placeholder':'email@.correo'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Ingresa tu(s) nombre'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Ingresa tu(s) apellido'})
        }
        help_texts={
            'username':'maximo 150 carateres',
            'password':'minimo 8 caracteres'
        }