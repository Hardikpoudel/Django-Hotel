from rest_framework.routers import DefaultRouter
from .views import reservationList

router = DefaultRouter()
router.register('reservationList', reservationList, basename='list')

urlpatterns = router.urls
