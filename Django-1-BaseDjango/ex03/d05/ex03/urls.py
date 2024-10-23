from django.urls import path
from .views import color_table


urlpatterns = [
    path('ex03/', color_table, name="Color table"),
]
