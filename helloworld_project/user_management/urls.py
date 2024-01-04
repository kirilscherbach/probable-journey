from django.urls import path

from .views import CustomLoggedOutView, CustomLoginView, SignUpView, profile

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLoggedOutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", profile, name="profile"),
]
