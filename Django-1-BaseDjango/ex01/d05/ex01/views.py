from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def django_framework(request):
    template = loader.get_template('django.html')
    return HttpResponse(template.render())


def static_page(request):
    template = loader.get_template('display.html')
    return HttpResponse(template.render())