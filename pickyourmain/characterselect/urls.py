from django.urls import path 
from django.contrib import admin

from . import views

urlpatterns = [
path('', views.select, name='select'),
path('character/<str:char>', views.character, name="character")
]