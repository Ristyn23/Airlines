from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings

from airtickets.views import AeroportListView

urlpatterns = [
    path('api/aeroport/', AeroportListView.as_view()),
    path('admin/', admin.site.urls),
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
