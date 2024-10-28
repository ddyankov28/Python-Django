from django.urls import path
from .views import init_view


urlpatterns = [
    path('ex00/init/', init_view, name="init")
]
