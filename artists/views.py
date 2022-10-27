from django.http import HttpResponse
from django.shortcuts import render
from .forms import artistForm
from .models import Artist
from django.views import View

class allArtists(View):
    form = artistForm
    template = 'getAllArtist.html'
    model = Artist
    
    def get(self, request):
        data = self.model.objects.all().prefetch_related('albums_set')
        return render(request, self.template, {'allArtist': data})


class createArtist(View):
    form = artistForm
    template = 'createArtist.html'

    def get(self, request):
        if request.user.is_authenticated:
            newArtist = self.form()
            return render(request, self.template, {'artistForm': newArtist})
        else:
            return HttpResponse('Unauthenticated user, please login to access this page.')

    def post(self, request):
        if request.user.is_authenticated:
            newArtist = self.form(request.POST)
            if newArtist.is_valid():
                newArtist.save()
            return render(request, self.template, {'artistForm': newArtist})
        else:
            return HttpResponse('Unauthenticated user, please login to access this page.')
