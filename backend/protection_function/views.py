from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *


# Create your views here.
class ProtectionToolFunctionViewSet(viewsets.ModelViewSet):
    queryset = ProtectionToolFunction.objects.all()
    serializer_class = ProtectionToolFunctionSerializer
