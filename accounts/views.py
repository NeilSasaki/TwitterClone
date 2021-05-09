from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from .forms import RegistForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm


class HomeView(TemplateView):
    template_name = 'accounts/home.html'


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(120000)
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    pass


class RegistUserView(CreateView):
    template_name = 'accounts/regist.html'
    form_class = RegistForm


class UserView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/user.html'

    def dispatch(self,  *args, **kwargs):
        return super().dispatch(*args,**kwargs)