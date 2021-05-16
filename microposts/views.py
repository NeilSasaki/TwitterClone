from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView, View
from .forms import PostCreateForm, PostUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post, Like
from accounts.models import Users, Relationship
from django.http.response import JsonResponse


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
    # テンプレートでは、object_listとしてreturnの値が渡される
    def queryset(self):
        return Post.objects.all()
    # get_context_dataは複数のデータをテンプレートにcontextとして
    # 送りたいときに使う。１つだけでよければ、createviewではqueryset
    # でobject_listとして渡すことができる。
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['favorite_list'] = user.favoritePost.all()
        # Postsテーブルの全データを取得しpost_listへ格納
        context['posts_list'] = Post.objects.all()
        return context


class MyPostListView(LoginRequiredMixin, ListView):
    # テンプレートを指定
    template_name = 'microposts/myposts.html'
    # 利用するモデルを指定
    model = Post

    success_url = reverse_lazy('microposts:myposts')

    # Postsテーブルのowner_idが自分自身の全データを取得するメソッド定義
    def get_queryset(self):
        return Post.objects.filter(owner_id=self.request.user)

    # def get_object(self):
    #     print(self.request.user)
    #     return self.request.user


# class FollowersView(LoginRequiredMixin, ListView):
#     # テンプレートを指定
#     template_name = 'microposts/followers.html'
#     # 利用するモデルを指定
#     model = Users
#
#     # Postsテーブルの全データを取得するメソッド定義
#     def queryset(self):
#         return Users.objects.filter(touser_id = self.request.user)

class FollowersView(LoginRequiredMixin, ListView):
    # テンプレートを指定
    template_name = 'microposts/followers.html'
    # 利用するモデルを指定
    model = Relationship

    # Postsテーブルの全データを取得するメソッド定義
    def queryset(self):
        return Relationship.objects.filter(user_id=(self.request.user))


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'microposts/update.html'

    def form_valid(self, form):
        messages.success(self.request, '更新が完了しました')
        return super(PostUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, '更新が失敗しました')
        return redirect('microposts:create')

    def get_success_url(self):
        return reverse_lazy('microposts:update', kwargs={'pk': self.object.id})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'microposts/delete.html'
    # deleteviewでは、SuccessMessageMixinが使われないので設定する必要あり
    success_url = reverse_lazy('microposts:myposts')
    success_message = "投稿は削除されました。"

    # 削除された際にメッセージが表示されるようにする。
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

# class LikeView(LoginRequiredMixin, CreateView):
#     model = Like
#     success_url = reverse_lazy('microposts:list')
#     success_message = "お気に入りに追加しました"
#
#     def get(self):
#
#
#     # def post(self, request):
#     #     post_id = request.POST.get('id')
#     #     post = Post.objects.get(id=post_id)
#     #     like = Like(Users=self.request.user, post=post)
#     #     like.save()
