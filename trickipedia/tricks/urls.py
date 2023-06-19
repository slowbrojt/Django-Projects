from django.urls import path 
from django.contrib import admin

from . import views

urlpatterns = [
path('', views.index, name='index'),
path('submissions', views.trickform, name="trickform"),
path("login", views.login_view, name="login"),
path("logout", views.logout_view, name="logout"),
path("review", views.review, name="review"),
path("success", views.success, name="success"),
path("review/<int:trick_id>", views.reviewtrick, name="adminreview"),
path("delete/<int:trick_id>", views.delete, name="delete"),
path("trick/<int:trick_id>", views.trick, name="trick") 
]