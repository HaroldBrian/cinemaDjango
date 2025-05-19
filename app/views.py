from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.models import Author, Movie
from app.serializers import AuthorSerializer, MovieSerializer

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def destroy(self, request, *args, **kwargs):
        author = self.get_object()
        # Check if the author has any movies associated with movies
        if author.movie_set.exists():
            return Response(
                {'error': "Cannot delete author with associated movies."},
                status=status.HTTP_400_BAD_REQUEST
            )        
        return super().destroy(request, *args, **kwargs)
    
     
class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['status']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by status if provided in the query parameters
        # Example: /api/movies/?status=published
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset
    
    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        """
        Archive a movie
        """
        movie = self.get_object()
        movie.status = 'archived'
        movie.save()
        serializer = self.get_serializer(movie)
        data = serializer.data
        data['message'] = 'Movie archived successfully.'
        return Response(data, status=status.HTTP_200_OK)
    
# register a new user
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'message': 'User created successfully',
            'token': token.key
        }, status=status.HTTP_201_CREATED)