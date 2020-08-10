from django.shortcuts import render
from django.http import HttpResponse

def error(request):
    return HttpResponse("error")