from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('hotels', HotelView)
router.register('rooms', RoomView)
router.register('room-types', RoomTypeView)

urlpatterns = router.urls
