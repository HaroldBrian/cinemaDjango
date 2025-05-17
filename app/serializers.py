from rest_framework import serializers
from app.models import Author, Movie

# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'email', 'birth_date']
        
# Serializer for Movie model
class MovieSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'rating', 'author', 'status']