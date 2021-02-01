from rest_framework.routers import DefaultRouter
from diningHall_api.views import hallList, hallReservationList

router = DefaultRouter()
router.register('hallList', hallList, basename='list')
router.register('hallReserv', hallReservationList, basename='reserv')


urlpatterns = router.urls
