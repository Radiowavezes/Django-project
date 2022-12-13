from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)

urlpatterns += [
        path('', views.index, name='index'),
        path('login/', views.signin, name="login"),
        path('logout/', views.signout, name='logout'),
        path('signup/', views.signup, name='signup'),
]

urlpatterns += [
        path('leave_feedback/', views.leave_feedback, name='leave_feedback'),
]