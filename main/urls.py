from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.signup, name='signup'),
    path('create-post/', views.createpost, name='createpost'),
]
