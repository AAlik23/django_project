from django.shortcuts import render
from django.http import HttpResponse
import time

def home(request):
    return HttpResponse('<h1>Hello, Home</h1>')


def about(request):
    return HttpResponse('<h1>about page</h1>')

def hndik(request):
    return HttpResponse('<h1>heyy miss you indeyka <3</h1>')
# Create your views here.
