from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProtectionToolViewSet(viewsets.ModelViewSet):
    queryset = ProtectionTool.objects.all()
    serializer_class = ProtectionToolSerializer
    # pagination_class = StandardResultsSetPagination
    http_method_names = ['get', 'put', 'patch', 'delete', 'head', 'options', 'trace']