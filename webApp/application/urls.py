from django.urls import path
from .views import post_SignUp, get_RegisteredUsers, post_UserInfo, post_EditUser, index


app_name = 'application'
urlpatterns = [
    path('', index, name='index'),
    path('signup.html', post_SignUp, name='sign_up'),
    path('edit/', post_EditUser, name='edit'),
    path('register/', get_RegisteredUsers, name='register'),
    path('info/', post_UserInfo, name='info'),
]
