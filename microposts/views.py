from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages



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
