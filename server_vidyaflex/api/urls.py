from django.urls import path
from . import views

# import views from .views

urlpatterns = [path("", views.index, name="index")]
