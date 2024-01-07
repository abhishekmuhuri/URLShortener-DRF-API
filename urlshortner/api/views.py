from .models import User, URL
from .serializers import UserSerializer, URLSerializer
from rest_framework import generics, permissions
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
        print(request.data)
        serializer = URLSerializer(data=request.data)
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
            url_object = URL.objects.get(alias=pk)
            serializer = URLSerializer(url_object)
            return Response(serializer.data)
        except URL.DoesNotExist:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
