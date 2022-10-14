from django.shortcuts import render
from django.http import HttpResponse

def artist(request):
    return HttpResponse('Welcome From Artist Page.')

    #return render()
    #
    #