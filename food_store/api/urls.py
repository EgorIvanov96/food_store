from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (UserCustomViewSet, DirectoryViewSet,
                    CategoriesViewSet, ProductsViewSet)

app_name = 'api'

router = DefaultRouter()

router.register('users', UserCustomViewSet, basename='users')
router.register('catalog', DirectoryViewSet, basename='catalog')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('products', ProductsViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
