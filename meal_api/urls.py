from rest_framework.routers import DefaultRouter
from .views import mealTypeList, mealList

router = DefaultRouter()
router.register('mealType', mealTypeList, basename='mealTyp')
router.register('meal', mealList, basename='meal')

urlpatterns = router.urls
