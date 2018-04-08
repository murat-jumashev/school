from django.urls import path

from . import views

urlpatterns = [
    path('aidar', views.index, name='index'),
]
