from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', include('tournament.urls')),
    path('admin/', admin.site.urls, name='admin'),
]
