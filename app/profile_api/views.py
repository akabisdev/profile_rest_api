from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from profile_api import serializers
from profile_api import models
from profile_api import permissions


class HelloAPIView(APIView):
    """Test API VIEW"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of APIVIEW"""

        an_apiview = [
            'Uses HTTP methods as functions(GET,POST,PUT,PATCH and DELETE)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': an_apiview})

    def post(self, request):
        """Create hello message with name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': message})

        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'Failed', 'data': serializer.errors})

    def put(self, request, pk=None):
        """Updates an object"""

        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': 'PUT method'})

    def patch(self, request, pk=None):
        """Used to partially update an object"""

        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': 'PATCH method'})

    def delete(self, request, pk=None):
        """Used to delete an object"""
        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': 'DELETE method'})


class HelloViewSet(viewsets.ViewSet):
    """Test view set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Similar to GET request,represent an action, i.e return all data"""
        viewset_features = [
            'Use actions like: list, create, update, partially_update, retrieve, destroy, instead of GET, POST, PUT, PATCH, & DELETE',
            'Automaticllly map to url with the help of router',
            'More functionality with less code',
            'Used where simple operations(CRUD features has to be performed)'
        ]

        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': viewset_features})

    def create(self, request):
        """Action to create new entry"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': message})
        else:
            return Response(
                {'status': status.HTTP_400_BAD_REQUEST,
                 'message': 'Failed',
                 'data': serializer.errors})

    def retrieve(self, request, pk=None):
        """Action to get any particular entry"""
        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': 'HTTP GET method'})

    def update(self, request, pk=None):
        """action to update any object"""
        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': 'HTTP PUT method'})

    def partial_update(self, request, pk=None):
        """action to partial update"""
        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': 'HTTP PATCH method'})

    def destroy(self, request, pk=None):
        """action to delete entry"""
        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'data': 'HTTP DELETE method'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handle creating user auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class UserFeedViewSet(viewsets.ModelViewSet):
    """Viewset for creating listing user status feed"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserFeedSerializer
    queryset = models.UserFeedModel.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """customize create request for the user feed"""
        
        serializer.save(user_profile=self.request.user)


