from django.shortcuts import render

from typing import Any

from django.http import HttpResponse


def about(request: Any) -> HttpResponse:
    return render(request, 'pages/about.html')


def rules(request: Any) -> HttpResponse:
    return render(request, 'pages/rules.html')
