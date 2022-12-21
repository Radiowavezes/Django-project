from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


favicon_view = RedirectView.as_view(url="/static/images/favicon.ico", permanent=True)

urlpatterns = ([
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("posy.urls", namespace="posy")),
    path("store/", include("store.urls", namespace="store")),
    re_path(r"^favicon\.ico$", favicon_view),
]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
)