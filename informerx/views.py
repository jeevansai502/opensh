from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse

from .models import PageView
# Create your views here.
def health(request):
    return HttpResponse(1)
