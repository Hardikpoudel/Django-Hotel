from rest_framework.routers import DefaultRouter
from .views import eventList, eventReservationList

router = DefaultRouter()
router.register('eventList', eventList, basename='list')
router.register('eventReserv', eventReservationList, basename='reserv')
urlpatterns = router.urls
