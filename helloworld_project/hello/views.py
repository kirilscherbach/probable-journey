from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    context = {}
    context["current_time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render(request, "hello/hello.html", context)


def monthly_challenge(request, month):
    return HttpResponse(f"hello, {month}")
