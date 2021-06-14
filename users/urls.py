from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    path('', views.LoginUser, name='users-home'),
    path('login/', views.LoginUser, name='login'),
    path('register/', views.RegisterUser, name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    path('profile/edit', views.Edit_Profile, name='profile'),
    path('setting/', views.Setting, name='setting')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

