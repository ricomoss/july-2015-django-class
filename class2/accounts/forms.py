from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, help_text='Choose a username.')
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(), help_text='Enter a password.')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
