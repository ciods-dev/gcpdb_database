from django.urls import path
from . import views

app_name = 'gcpdb'

urlpatterns = [
    path('quick_search/',views.quick_search, name='quick_search'),
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('faq/',views.faq,name='faq'),
    path('bquery/',views.bquery,name='bquery')
    ]
