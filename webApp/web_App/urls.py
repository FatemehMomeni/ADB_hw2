from django.contrib import admin
from django.urls import path, include
from application import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.sign, name='signup'),
    path('signup.html', views.post_SignUp, name='sign_up'),
    path('register.html', views.get_RegisteredUsers, name='register'),
    path('editation/', views.edition, name='editation'),
    path('edit.html', views.post_EditUser, name='edit'),
    path('update.html', views.update, name='update'),
    path('info/', views.information, name='information'),
    path('info.html', views.post_UserInfo, name='info'),
]
# path('regist', views.regist, name='regist'),
