from django.urls import path

from . import views

# creating URLconf
urlpatterns = [
    path("", views.hello_world, name="hello_world"),
]
