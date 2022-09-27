from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import dashboard, register, update_url, play_pause_check, \
    delete_url, update_interval

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("login/", LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="main/logout.html"), name="logout"),
    path("register/", register, name="register"),

    path("update/url/<int:pk>/", update_url, name="update_url"),
    path("playpause/url/<int:pk>/", play_pause_check, name="play_pause_check"),
    path("delete/url/<int:pk>/", delete_url, name="delete_url"),
    path("updateinterval/url/<int:pk>/", update_interval, name="update_interval"),
]