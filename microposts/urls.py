from django.urls import path
from .views import (
    PostCreateView, PostListView, MyPostListView,
    PostDeleteView
)
from . import views

app_name = 'microposts'
urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('list/', PostListView.as_view(), name='list'),
    path('myposts/', MyPostListView.as_view(), name='myposts'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
]
