from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "gallery"
urlpatterns = [
    path("list/", views.GalleryListView.as_view(), name="image_list"),
    path("", views.GalleryListView.as_view(), name="image_list"),
    path('upload/', views.upload, name="upload"),
    path('<slug:date>/<slug:filename>/', views.upload_detail, name="image_details"),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
