from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.home),
    path('login/',views.login),
    path('signup/',views.signup),
    path('logout/',views.logout),
    path('logo/',views.logo),
    path('aboutus/', views.aboutus),
    path('index/', views.index),
   

]