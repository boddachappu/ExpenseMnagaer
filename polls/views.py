from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('U are in first page of application')


def about(request):
    return HttpResponse('It is in progress')