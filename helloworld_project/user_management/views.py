from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


class CustomLoggedOutView(LogoutView):
    template_name = "registration/logged_out.html"


@login_required
def profile(request):
    return render(request, "user_management/profile.html", {"user": request.user})
