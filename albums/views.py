from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from django.forms import ValidationError
from .serializers import AlbumSerializer
from .filters import AlbumsFilters
from .models import Albums

class allAlbums(generics.ListAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Albums.objects.filter(approved=True)
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    filterset_class = AlbumsFilters

    def get(self, request):
        return self.list(request) 

    def post(self, request):
        if not hasattr(request.user, 'artist'):
            return Response(data={'message': 'To add album, you must be an artist.'}, status=403)
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(artist=self.request.user.artist)
            return Response(serializer.data, status=201) 
        else:
            return Response({"message": "Unauthorized User."})


class AlbumListManual(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get(self, request):        
        queryset = Albums.objects.filter(approved = True)

        name = request.query_params.get('name')
        gte = request.query_params.get('cost_gte')
        lte = request.query_params.get('cost_lte')

        try:
            if gte:
                queryset = queryset.filter(cost__gte=gte).all()
            if lte:
                queryset = queryset.filter(cost__lte=lte).all()
            if name:
                queryset = queryset.filter(name__iexact= name).all()  
        except:
            return Response({'message': "Wrong cost or name values."})   

        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)