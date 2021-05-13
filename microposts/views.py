from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'microposts/create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('microposts:create')

    def form_valid(self, form):
        # formに問題なければ、owner id に自分のUser idを割り当てる
        # ここは、左側はusers.idではなくuser.idで良い。
        # request.userが一つのセットでAuthenticationMiddlewareでセットされている。
        form.instance.owner_id = self.request.user.id
        messages.success(self.request, '投稿が完了しました')
        return super(PostCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, '投稿が失敗しました')
        return redirect('microposts:create')


class PostListView(LoginRequiredMixin, ListView):
    # テンプレートを指定
    template_name = 'microposts/list.html'
    # 利用するモデルを指定
    model = Post

    # Postsテーブルの全データを取得するメソッド定義
    def queryset(self):
        return Post.objects.all()


class MyPostListView(LoginRequiredMixin, ListView):
    # テンプレートを指定
    template_name = 'microposts/myposts.html'
    # 利用するモデルを指定
    model = Post

    # Postsテーブルの全データを取得するメソッド定義
    def queryset(self):
        return Post.objects.filter(owner_id = self.request.user)

    # def get_object(self):
    #     print(self.request.user)
    #     return self.request.user