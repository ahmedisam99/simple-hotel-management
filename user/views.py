from rest_framework.viewsets import ModelViewSet

from .serializers import *


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
