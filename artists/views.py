from django.http import HttpResponse
from django.shortcuts import render
from .forms import artistForm
from .models import Artist

def artist(request):
    data = Artist.objects.all().prefetch_related('albums_set')
    return render(request, 'getAllArtist.html', {'allArtist': data})
    

def createArtist(request):
    if request.method == 'POST':
        Stage_name = request.POST.get('Stage_name')
        Social_link = request.POST.get('Social_link')

        newArtist = Artist(Stage_name = Stage_name, Social_link = Social_link)
        newArtist.save()

    return render(request, 'createArtist.html', {'artistForm': artistForm})
