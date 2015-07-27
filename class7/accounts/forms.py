from django import forms

from accounts import models


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, help_text='Choose a username.')
    email = forms.EmailField()
    password1 = forms.CharField(
        widget=forms.PasswordInput(), help_text='Enter a password.',
        label='Password')
    password2 = forms.CharField(
        widget=forms.PasswordInput(), label='Password',
        help_text='Confirm your password.')

    def _handle_username(self, username):
        if models.User.objects.filter(username=username).exists():
            msg = 'Username {} has already been taken.  Please try again.'
            self._errors['username'] = [msg.format(username)]
            return

    def _handle_password(self, password1, password2):
        if not (password1 and password2) or (password1 != password2):
            msg = 'Passwords do not match.  Please try again.'
            self._errors['password2'] = [msg]
            return

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        self._handle_password(password1, password2)

        username = cleaned_data.get('username')
        self._handle_username(username)

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        if username:
            try:
                user = models.User.objects.get(username=username)
            except models.User.DoesNotExist:
                msg = 'Invalid username.'
                self._errors['username'] = [msg]
                return cleaned_data
        else:
            return cleaned_data

        password = cleaned_data.get('password')
        if password:
            if not user.check_password(password):
                msg = 'Invalid password.'
                self._errors['password'] = [msg]
        return cleaned_data
