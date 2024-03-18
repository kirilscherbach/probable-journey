from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("user:login")
    template_name = "registration/signup.html"


@login_required
def profile(request):
    print(request.user)
    print(request.user.is_authenticated)
    print(request.session.session_key)
    print(request.COOKIES)
    return render(request, "user_management/profile.html", {"user": request.user})
