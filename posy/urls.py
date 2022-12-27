from django.urls import path
from posy.views.home import home
from posy.views.index import index
from posy.views.signin import signin
from posy.views.signout import signout
from posy.views.signup import signup
from posy.views.leave_feedback import leave_feedback
from django.conf import settings
from django.conf.urls.static import static


app_name = "posy"
urlpatterns = ([
        path("", home, name="home"),
        path("", index, name="index"),
        path("login/", signin, name="login"),
        path("logout/", signout, name="logout"),
        path("signup/", signup, name="signup"),
        path("leave_feedback/", leave_feedback, name="leave_feedback"),
    ]
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # + static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
)
