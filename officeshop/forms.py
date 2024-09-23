from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
        attrs={
            'autocomplete': 'text',
            'placeholder': 'Введите логин',
            }
        ),
        required=False,
        validators=[RegexValidator(r'[^0-9а-яА-ЯёЁ]', "Введите логин латиницей")],
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
        attrs={
            'autocomplete': 'email',
            'placeholder': 'Введите электронную почту',
            }
        ),
        required=False
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль',
            }
        ),
        required=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Повторите пароль',
            }
        ),
        required=False
    )
    def clean_password1(self):
        password = self.cleaned_data['password1']
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Введите логин', code='invalid')
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError('Введите электронную почту', code='invalid')
        return email
    
    class  Meta(UserCreationForm.Meta): 
        fields=("username", "email", "password1", "password2")