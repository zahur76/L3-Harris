from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("method_two", views.method_two, name="method_two"),
]