
from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# def index(request):
#     template = loader.get_template('algoritmos/index.html')
#     return HttpResponse(template.render())

def index_view(request):
    template = loader.get_template('algoritmos/index.html')
    return HttpResponse(template.render())

def busquedas_view(request):
        template = loader.get_template('algoritmos/busquedas.html')
        return HttpResponse(template.render())
