from django.urls import path
from .views import *
from . import views

from django.contrib import admin
from django.urls import path, include


app_name = 'info'

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('login/', views.my_login,name='login'),
    path("signup/", views.signup, name="signup"),
    path('service/',views.service,name='service'),
    path('guide/',views.guide,name='guide'),
    ]
