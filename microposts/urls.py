from django.urls import path
from .views import (
    PostCreateView, PostListView, MyPostListView,
    PostDeleteView, PostUpdateView,
)
from . import views

app_name = 'microposts'
urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('list/', PostListView.as_view(), name='list'),
    path('myposts/', MyPostListView.as_view(), name='myposts'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    # path('like/', LikeView.as_view(), name='like')
]
