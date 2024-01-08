from .models import User, URL
from .serializers import UserSerializer, URLSerializer, UserRegistrationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class urlAPI(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            # Valid data, create and save the URL object
            url_object = serializer.save()
            serialized_data = URLSerializer(url_object).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            # Invalid data, return error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, pk):
        try:
            url_object = URL.objects.get(alias=pk)
            serializer = URLSerializer(url_object)
            return Response(serializer.data)
        except URL.DoesNotExist:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)

class UserAPI(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)