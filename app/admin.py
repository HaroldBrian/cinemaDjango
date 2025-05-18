from django.contrib import admin
from .models import Author, Movie

class MovieInline(admin.TabularInline):
    model = Movie
    extra = 0
    readonly_fields = ['title', 'description', 'release_date', 'rating', 'status']
    can_delete = False
    show_change_link = True

class RatingFilter(admin.SimpleListFilter):
    title = 'Évaluation'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(rating=self.value())
        return queryset

class StatusFilter(admin.SimpleListFilter):
    title = 'Statut'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return Movie.STATUS_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'birth_date']
    inlines = [MovieInline]

class MovieAdmin(admin.ModelAdmin):
    list_filter = ['release_date', RatingFilter, StatusFilter]
    list_display = ['title', 'description', 'release_date', 'rating', 'author', 'status']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Movie, MovieAdmin)