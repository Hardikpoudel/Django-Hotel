from rest_framework.routers import DefaultRouter
from .views import guestList

router = DefaultRouter()
router.register('guestList', guestList, basename='list')

urlpatterns = router.urls
