from django.db.models import Prefetch
from django.core.paginator import Paginator
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.shortcuts import render ,redirect

from .models import Gcpdb
from .serializers import GcpdbSerializers

def home(request):
    return render(request,'gcpdb/home.html')   

def faq(request):
    return render(request,'gcpdb/faq.html')   

# def quick_search(request):

# to test

# http://localhost:8000/gcpdb/quick_search/?protein=A0A075B6K6

# as of now i have developed only for uniprot . develop for refseq also

def quick_search(request):  

    protein = request.GET.get('protein')
    print(protein)
    if protein:
        qs = Gcpdb.objects.filter(uniprot__uniprot_id=protein)
        context = {'data' :qs }
        return render(request, 'gcpdb/qs_result.html',context)



def batch_queury(request):
    protein = request.GET.get('proteins')
    if protein:
        proteins = [i.strip() for i in protein.split()]

        qs = Gcpdb.objects.filter(uniprot__uniprot_id__in=proteins)
        context = {'data' :qs }
        return render(request, 'gcpdb/batch_query_result.html',context)

