from django.shortcuts import render
from django.http import HttpResponse
from .forms import albumForm
from .models import Albums

def albums(request):
    return HttpResponse('Welcome From Albums Page.')

def createAlbum(request):
    if request.method == 'POST':
        newAlbum = albumForm(request.POST)
        if newAlbum.is_valid():
            newAlbum.save()
    else:
        newAlbum = albumForm()

    return render(request, 'createAlbum.html', {'albumForm': newAlbum})
