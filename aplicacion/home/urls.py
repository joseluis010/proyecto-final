from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register, name="register"),
    path('buscar/', views.buscar, name='buscar'),
    path('agregar/', views.agregar_informacion, name='agregar'),
    path("logout/", LogoutView.as_view(template_name="home/index.html"), name="logout"),
    
]+ staticfiles_urlpatterns()