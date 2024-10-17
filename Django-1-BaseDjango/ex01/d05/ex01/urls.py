from django.urls import path
from . import views

urlpatterns = [
    path('ex01/django', views.ex01, name='Django, framework'),
]