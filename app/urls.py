from django.urls import re_path,path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('register',views.register_user,name = 'register')
]   