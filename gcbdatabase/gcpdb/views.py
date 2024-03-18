from django.shortcuts import render ,redirect
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
import os
from django.conf import settings
from django.http import HttpResponse
from django.http import Http404

# from .models import Gcpdb

def home(request):
    return render(request,'gcpdb/home.html')