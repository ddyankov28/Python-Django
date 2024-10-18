from django.urls import path
from . import views

urlpatterns = [
    path('ex01/django/', views.django_framework, name='Django framework'),
    path('ex01/display/', views.static_page, name='Static page'),
    path('ex01/templates/', views.templates_page, name='Templates page'),
]
