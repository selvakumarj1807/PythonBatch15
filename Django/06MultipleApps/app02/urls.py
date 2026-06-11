from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.app02_index),
]