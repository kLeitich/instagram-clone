from django.urls import re_path,path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('register',views.register_user,name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]   