from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>', views.showchoices, name="showchoices"),
    path('<int:question_id>/result', views.voted, name="voted"),
    
]
