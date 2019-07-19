from rest_framework.routers import DefaultRouter

from .views import UserView

router = DefaultRouter()
router.register('users/all', UserView)

urlpatterns = router.urls
