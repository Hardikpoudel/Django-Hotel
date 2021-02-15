from rest_framework.routers import DefaultRouter
from .views import roomTypeList, roomList, imageList

router = DefaultRouter()

router.register('img', imageList, basename='img')
router.register('typeList', roomTypeList, basename='typeList')
router.register('room', roomList, basename='room')


urlpatterns = router.urls
