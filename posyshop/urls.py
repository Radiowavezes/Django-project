from django.contrib import admin
from django.urls import path, include

app_name = 'posy'
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('posy.urls')),
    path('cart/', include('shopping_cart.urls')),
    path('unicorn/', include('django_unicorn.urls')),
] 
