from rest_framework import serializers
from models import ProtectionToolCertificate
from backend.protection_tool.serializers import ProtectionToolSerializer


class ProtectionToolCertificateSerializer(serializers.ModelSerializer):
    tool = ProtectionToolSerializer(read_only=True)

    class Meta:
        model = ProtectionToolCertificate
        fields = '__all__'
