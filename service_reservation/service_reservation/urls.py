from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include("site_reservation.urls")),
    path("reservation/", include("site_reservation.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




