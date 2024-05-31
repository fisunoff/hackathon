from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *


# Create your views here.
class ProtectionToolCertificateViewSet(viewsets.ModelViewSet):
    queryset = ProtectionToolCertificate.objects.all()
    serializer_class = ProtectionToolCertificateSerializer


class ProtectionToolCertificateDiffViewSet(viewsets.ModelViewSet):
    queryset = ProtectionToolCertificateDiff.objects.all()
    serializer_class = ProtectionToolCertificateDiffSerializer
