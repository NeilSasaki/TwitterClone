from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
import microposts.models
from .forms import RegistForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from microposts.models import Post
from .models import Users


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


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/user.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def AddFavorite(request, pk):
    # postのpkをhtmlから取得
    post = get_object_or_404(Post, pk=pk)
    # ログインユーザーを取得
    user = request.user
    # ログインユーザーをfavoritePostのUser_idとして、post_idは
    # 上で取得したPostを記録
    user.favoritePost.add(post)
    return redirect('microposts:list')


def RemoveFavorite(request, pk):
    # postのpkをhtmlから取得
    post = get_object_or_404(Post, pk=pk)
    # ログインユーザーを取得
    user = request.user
    # ログインユーザーをfavoritePostのUser_idとして、post_idは
    # 上で取得したPostを記録
    user.favoritePost.remove(post)
    return redirect('microposts:list')
