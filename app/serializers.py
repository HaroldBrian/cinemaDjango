from rest_framework import serializers
from app.models import Author, Movie

# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'birth_date']
        
# Serializer for Movie model
class MovieSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True, source='author'
    )
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'rating', 'author', 'author_id', 'status']