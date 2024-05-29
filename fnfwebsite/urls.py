from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include






urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('fnfwebapp.urls', namespace = 'fnfwebapp')),
    path('', include('basket.urls', namespace = 'basket')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
