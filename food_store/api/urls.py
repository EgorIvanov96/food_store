from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (UserCustomViewSet, DirectoryViewSet,
                    CategoriesViewSet, ProductsViewSet,
                    CartViewSet)

app_name = 'api'

router = DefaultRouter()

router.register('users', UserCustomViewSet, basename='users')
router.register('catalog', DirectoryViewSet, basename='catalog')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('products', ProductsViewSet, basename='products')
router.register(r'carts', CartViewSet, basename='carts')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path(
        'carts/<int:cart_id>/items/<int:item_id>/',
        CartViewSet.as_view({'delete': 'destroy'}),
        name='cart-item-delete'
        )
]
