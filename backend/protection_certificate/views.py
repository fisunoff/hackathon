from django.shortcuts import render
from serializers import ProtectionToolCertificateSerializer
from rest_framework import viewsets
from models import ProtectionToolCertificate


# Create your views here.
class ProtectionCertificateViewSet(viewsets.ModelViewSet):
    queryset = ProtectionToolCertificate.objects.all()
    serializer_class = ProtectionToolCertificateSerializer
