from django.shortcuts import render
from django.http import HttpResponse

def mypagefucntion(request):
    return HttpResponse("Hello world!")
