from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def ex01(request):
    template = loader.get_template('django.html')
    return HttpResponse(template.render())