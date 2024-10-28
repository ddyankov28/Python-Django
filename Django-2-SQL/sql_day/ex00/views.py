from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from django.conf import settings


def init_view(request):
    db_params = {
        'dbname' : settings.DATABASES['default']['NAME']
    }