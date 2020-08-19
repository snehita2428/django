from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mycontacts import views
urlpatterns = [
    url(r'names.*', views.names, name='names'),
    url(r'numbers.*', views.numbers, name='numbers'),
]