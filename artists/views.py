from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .serializers import ArtistSerializer
from .forms import artistForm
from .models import Artist

class allArtists(APIView):
    form = artistForm
    template = 'getAllArtist.html'
    model = Artist

    def get(self, request, format=None):
        data = self.model.objects.all()
        serializer = ArtistSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


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