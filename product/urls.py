from django.contrib import admin
from django.urls import path,include
from .views import index,login,register


urlpatterns = [
    path('',index,name='home'),
    path('login/',login,name='login'),
    path('reg/',register,name='register'),
]