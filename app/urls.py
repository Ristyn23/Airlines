from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings

from airtickets.api import AeroportViewSet, FlightViewSet, PlaneViewSet, SeatViewSet, TicketViewSet, ProfileViewSet

router = DefaultRouter()
router.register('aeroports', AeroportViewSet, 'aeroports')
router.register('flights', FlightViewSet, 'flights')
router.register('planes', PlaneViewSet, 'planes')
router.register('seats', SeatViewSet, 'seats')
router.register('tickets', TicketViewSet, 'tickets')
router.register('profile', ProfileViewSet, 'profile')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)