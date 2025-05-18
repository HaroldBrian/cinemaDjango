from django.contrib import admin
from .models import Author, Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_filter = ['release_date']
    list_display = ['title', 'description', 'release_date', 'rating', 'author', 'status']

admin.site.register(Author)
admin.site.register(Movie, MovieAdmin)