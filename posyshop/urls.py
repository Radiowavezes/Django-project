from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('posy.urls', namespace='posy')),
    path('store/', include('store.urls', namespace='store')),
]
