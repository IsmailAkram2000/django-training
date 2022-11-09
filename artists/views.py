from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArtistSerializer
from .models import Artist

class allArtists(APIView):
    def get(self, request):
        serailizer = ArtistSerializer(Artist.objects.all(), many=True)
        return Response(serailizer.data)


class createArtist(APIView):
    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        else:
            return Response(serializer.errors, 400)