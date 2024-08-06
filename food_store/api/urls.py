from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserCustomViewSet

app_name = 'api'

router = DefaultRouter()

router.register('users', UserCustomViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
