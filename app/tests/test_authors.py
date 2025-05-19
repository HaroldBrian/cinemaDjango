import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from app.models import Author

@pytest.mark.django_db
def test_create_author():
    client = APIClient()
    user = User.objects.create_user(username="brian", password="123")
    client.force_authenticate(user=user)

    response = client.post("/api/v1/authors/", {"name": "brian", "email": "brian@app.com", "birth_date": "2002-01-04"}, format="json")
    assert response.status_code == 201
    assert Author.objects.count() == 1

@pytest.mark.django_db
def test_get_authors():
    Author.objects.create(name="Author A", email="a@app.com", birth_date="2002-01-01")
    client = APIClient()
    response = client.get("/api/v1/authors/")
    assert response.status_code == 200
    assert len(response.data) == 1
