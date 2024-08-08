from djoser.views import UserViewSet
from rest_framework import viewsets

from users.models import User
from reviews.models import Categories, Directory, Products
from .serializers import (UserSerializer, ProductsSerializer,
                          DirectorySerializer, CategoriesSerializer)


class UserCustomViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DirectoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
