from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from accounts import forms, models


class RegisterView(View):
    template_name = 'accounts/register.html'
    form = forms.RegisterForm

    def get(self, request):
        return render(
            request, self.template_name, context={'form': self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = models.User.objects.create_user(username, email, password)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(
            request, self.template_name, context={'form': form})


class LoginView(View):
    template_name = 'accounts/login.html'
    form = forms.LoginForm

    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index'))
        return render(
            request, self.template_name, context={'form': self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(
            request, self.template_name, context={'form': form})


class LogoutView(View):
    @staticmethod
    def get(request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))
