from djoser.views import UserViewSet
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from reviews.models import Categories, Directory, Products, Cart, CartItem
from .serializers import (UserSerializer, ProductsSerializer,
                          DirectorySerializer, CategoriesSerializer,
                          CartSerializer)


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


class CartViewSet(viewsets.ModelViewSet):
    """Представление для корзины."""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, cart_id, item_id):
        try:
            cart = Cart.objects.get(id=cart_id, user=request.user)
            item = CartItem.objects.get(id=item_id, cart=cart)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
