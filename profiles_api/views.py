from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    # Test Api View

    def get(self, request, format=None):
        # Returns list of API features
        an_apiview = [
            'Uses HTTP methods such as (get, put, patch, post, and delete)',
            'Is similar to traditional Django views',
            'Gives the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
