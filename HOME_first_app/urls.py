from django.contrib import admin
from django.urls import path,include
from HOME_first_app import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('links', views.links,name='links'),
    
    

]