from django.urls import path
from .views import (
UserLoginView,UserLogoutView,RegistUserView,HomeView,UserView
)

app_name = 'accounts'
urlpatterns = [
    path('home/',HomeView.as_view(), name ='home'),
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
    path('user/', UserView.as_view(), name='user'),

]