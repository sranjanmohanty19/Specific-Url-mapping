from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>My mom is my mom</h1>')
def second(request):
    return HttpResponse('<h1>And I am her son</h1>')