from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from knox.auth import TokenAuthentication

class userDetail(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    
    def get(self, request, pk):
        if not request.user.pk == pk:        
            return Response({"Message": "Unauthorized User"}, status=401)
        user = User.objects.get(pk = pk)
        return Response({
            "id" : user.id,
            'username': user.username,
            'email': user.email,
            'bio' : user.bio
        }) 

    def put(self, request, pk):
        if not request.user.pk == pk:        
            return Response({"Message": "Unauthorized User"}, status=401)
        user = User.objects.get(pk = pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User Updated Successfully', 'Updated User': serializer.data}, status=200)
        
    def patch(self, request, pk):
        if not request.user.pk == pk:        
            return Response({"Message": "Unauthorized User"}, status=401)
        user = User.objects.get(pk = pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User Updated Successfully', 'Updated User': serializer.data}, status=200)