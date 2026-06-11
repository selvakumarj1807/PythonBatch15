from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.app01Index),
    path('/about', views.app01About)
]