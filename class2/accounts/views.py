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
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = models.User.objects.create_user(username, email, password)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.save()
        auth.login(request, user)
        return HttpResponseRedirect(reverse('index'))


class LoginView(View):
    template = 'accounts/login.html'
    form = forms.LoginForm

    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index'))
        context = {'form': self.form()}
        return render(request, self.template, context=context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return HttpResponseRedirect(reverse('index'))


class LogoutView(View):
    @staticmethod
    def get(request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))
