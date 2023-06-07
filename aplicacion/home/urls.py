from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register, name="register")
    
]+ staticfiles_urlpatterns()