from django.contrib import admin
from .views import *
from django.urls import path

from quiz import views

urlpatterns = [
    path('',views.home , name = 'home'), 
    path('answer',views.answer, name = 'answer'  ),
]
