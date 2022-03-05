from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('create-feed/', views.create, name='create'),
    path('myfeed/', views.myfeed, name='myfeed'),
    path('logout/', views.logout, name='logout')
]











