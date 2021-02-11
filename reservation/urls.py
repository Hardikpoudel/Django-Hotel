from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
# from django.conf.urls.static import static
# from django.conf import settings
from reservation import views
urlpatterns = [
    path('', TemplateView.as_view(template_name="reserve.html")),
    path('reserve', views.reservation, name='reserve')
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
