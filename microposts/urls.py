from django.urls import path
from .views import PostCreateView
from . import views

app_name = 'microposts'
urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
]