from django.urls import path

from djangoProject import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ViolinListCreate.as_view(), name='violin-list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)