from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *


# Create your views here.
class ProtectionToolViewSet(viewsets.ModelViewSet):
    queryset = ProtectionTool.objects.all()
    serializer_class = ProtectionToolSerializer
    http_method_names = ['get', 'put', 'patch', 'delete', 'head', 'options', 'trace']