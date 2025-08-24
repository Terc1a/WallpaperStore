from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:wallpaper_id>/", views.detail, name="detail"),
    path("download/<int:wallpaper_id>/", views.download, name="download"),
    path("sort/<int:tag_id>/", views.sort, name="sort"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)