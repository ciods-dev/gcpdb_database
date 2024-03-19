from django.urls import path
from . import views

app_name = 'gcpdb'

urlpatterns = [
    path('quick_search/',views.quick_search, name='quick_search'),
    ]
