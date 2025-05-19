import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from app.models import Author, Movie

@pytest.mark.django_db
def test_create_movie():
    client = APIClient()
    user = User.objects.create_user(username="harold", password="123")
    client.force_authenticate(user=user)

    author = Author.objects.create(name="FOTSEU CHEDJOU", email="fotseu@app.com", birth_date="2002-04-01")
    payload = {
        "title": "Iron Man 5 Movie",
        "description": "Iron Man 5",
        "release_date": "2025-05-20",
        "rating": 5,
        "author_id": author.id,
        "staus": "published"
    }

    response = client.post("/api/v1/movies/", payload, format="json")
    assert response.status_code == 201
    assert Movie.objects.count() == 1
