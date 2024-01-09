from .models import User, URL
from .serializers import UserSerializer, URLSerializer, UserRegistrationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShortURLList(generics.ListAPIView):
    authentication_classes = [BasicAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = URLSerializer

    def get_queryset(self):
        return URL.objects.filter(user=self.request.user.id)


class urlAPI(APIView):
    authentication_classes = [BasicAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = {
            'alias': request.data.get('alias'),
            'long': request.data.get('long'),
            'user': request.user.id
        }
        serializer = URLSerializer(data=data)
        if serializer.is_valid():
            # Valid data, create and save the URL object
            url_object = serializer.save()
            serialized_data = URLSerializer(url_object).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            # Invalid data, return error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            url_object = URL.objects.get(alias=pk,user=request.user.id)
            serializer = URLSerializer(url_object)
            return Response(serializer.data)
        except:
            return Response({'error':'alias not found'},status=status.HTTP_404_NOT_FOUND)

class UserAPI(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)