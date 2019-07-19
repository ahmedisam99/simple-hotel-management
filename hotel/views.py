from rest_framework.viewsets import ModelViewSet

from .serializers import *


class HotelView(ModelViewSet):
    queryset = Hotel
    serializer_class = HotelSerializer


class RoomTypeView(ModelViewSet):
    queryset = RoomType
    serializer_class = RoomTypeSerializer


class RoomView(ModelViewSet):
    queryset = Room
    serializer_class = RoomSerializer
