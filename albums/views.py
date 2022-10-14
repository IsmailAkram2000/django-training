from django.shortcuts import render
from django.http import HttpResponse

def albums(request):
    return HttpResponse('Welcome From Albums Page.')