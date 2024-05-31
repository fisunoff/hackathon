from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .serializers import *
from rest_framework import viewsets, status
from .models import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProtectionToolCertificateViewSet(viewsets.ModelViewSet):
    queryset = ProtectionToolCertificate.objects.all()
    serializer_class = ProtectionToolCertificateSerializer
    # pagination_class = StandardResultsSetPagination
    http_method_names = ['get', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class ProtectionToolCertificateDiffViewSet(viewsets.ModelViewSet):
    queryset = ProtectionToolCertificateDiff.objects.all()
    serializer_class = ProtectionToolCertificateDiffSerializer
    # pagination_class = StandardResultsSetPagination


class RecalcFunctionsView(APIView):
    def post(self, request):
        ProtectionToolCertificate.fill_functions_all()
        return Response(status=status.HTTP_200_OK)
