from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from app.views import AuthorViewSet, MovieViewSet
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'movies', MovieViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', obtain_auth_token),
]