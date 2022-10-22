from django.http import HttpResponse
from django.shortcuts import render
from .forms import artistForm
from .models import Artist

def artist(request):
    return HttpResponse('Welcome From Artist Page.')

def createArtist(request):
    Stage_name = request.POST.get('Stage_name')
    Social_link = request.POST.get('Social_link')

    newArtist = Artist(Stage_name = Stage_name, Social_link = Social_link)
    newArtist.save()

    return render(request, 'createArtist.html', {'artistForm': artistForm})
