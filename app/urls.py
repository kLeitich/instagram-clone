from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('register',views.register_user,name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/login.html'), name='logout'),
    path('profile',views.profile,name='profile'),
    path('update_profile/<int:id>',views.update_profile,name='update_profile'),
    path('dm',views.dm,name='dm'),
    path('image_upload',views.image_upload,name='image_upload'),
    path('explore',views.explore,name='explore'),
    path('notification',views.notification,name='notification'),
]   

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)