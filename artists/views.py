from django.http import HttpResponse
from django.shortcuts import render
from .forms import artistForm
from .models import Artist

def artist(request):
    data = Artist.objects.all().prefetch_related('albums_set')
    return render(request, 'getAllArtist.html', {'allArtist': data})
    

def createArtist(request):
    if request.method == 'POST':
        newArtist = artistForm(request.POST)
        if newArtist.is_valid():
            newArtist.save()
    else:
        newArtist = artistForm()

    return render(request, 'createArtist.html', {'artistForm': newArtist})