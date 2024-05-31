from rest_framework import serializers
from .models import ProtectionTool
from protection_certificate.models import ProtectionToolCertificate


class ProtectionToolCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectionToolCertificate
        fields = ['number', 'date_added', 'validity_period', 'documents',
                  'certification_schema', 'laboratory', 'agency', 'applicant',
                  'requisites', 'support_period', 'functions']


class ProtectionToolSerializer(serializers.ModelSerializer):
    certificates = ProtectionToolCertificateSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = ProtectionTool
        fields = ['title', 'certificates']


class BasicProtectionToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectionTool
        fields = ['title']
