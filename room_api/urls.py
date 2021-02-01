from rest_framework.routers import DefaultRouter
from .views import roomTypeList, roomList

router = DefaultRouter()
router.register('roomList', roomTypeList, basename='roomlist')
router.register('room', roomList, basename='room')


urlpatterns = router.urls
