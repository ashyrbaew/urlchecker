from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import dashboard, register, update_url, deactivate_url, delete_url

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("login/", LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="main/logout.html"), name="logout"),
    path("register/", register, name="register"),

    path("update/url/<int:pk>/", update_url, name="update_url"),
    path("deactivate/url/<int:pk>/", deactivate_url, name="deactivate_url"),
    path("delete/url/<int:pk>/", delete_url, name="delete_url"),
]