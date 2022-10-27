from django.shortcuts import render
from django.http import HttpResponse
from .forms import albumForm
from django.views import View

class albums(View):
    def get(self, request):
        return HttpResponse('Welcome From Albums Page.')

class createAlbum(View):
    form = albumForm
    template = 'createAlbum.html'

    def get(self, request):
        newAlbum = self.form()
        return render(request, self.template, {'albumForm': newAlbum})

    def post(self, request):
        newAlbum = self.form(request.POST)
        if newAlbum.is_valid():
            newAlbum.save()
        return render(request, self.template, {'albumForm': newAlbum})