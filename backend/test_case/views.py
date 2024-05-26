from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import TestCase
from .serializers import TestCaseSerializer


# Create your views here.
class TestCaseView(ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
