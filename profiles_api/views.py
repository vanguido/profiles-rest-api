from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    # Test Api View
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        # Returns list of API features
        an_apiview = [
            'Uses HTTP methods such as (get, put, patch, post, and delete)',
            'Is similar to traditional Django views',
            'Gives the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        # Create a hello message with our name
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        # Handle updating an object
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        # Handle a partial update of object
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        # Delete an object
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    # Test API view set
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        # Return a hello message
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps URLs using router',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        # Create a new hello message
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        # Handle getting an object by its ID
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        # Handle updating an object
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        # Handle partial update of an object
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        # Remove an object
        return Response({'http_method': 'DELETE'})
