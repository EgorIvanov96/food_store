from djoser.views import UserViewSet

from users.models import User
from .serializers import UserSerializer


class UserCustomViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
