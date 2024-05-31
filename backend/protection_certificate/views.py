from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import *
from rest_framework import viewsets, status
from .models import *


class ProtectionToolCertificateViewSet(viewsets.ModelViewSet):
    queryset = ProtectionToolCertificate.objects.all()
    serializer_class = ProtectionToolCertificateSerializer
    http_method_names = ['get', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class ProtectionToolCertificateDiffViewSet(viewsets.ModelViewSet):
    queryset = ProtectionToolCertificateDiff.objects.all()
    serializer_class = ProtectionToolCertificateDiffSerializer


class RecalcFunctionsView(APIView):
    def post(self, request):
        ProtectionToolCertificate.fill_functions_all()
        return Response(status=status.HTTP_200_OK)
