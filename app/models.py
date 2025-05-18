from django.db import models

# Class representing an Author
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name
    
# Class representing a Movie
class Movie(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)], default=5)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title