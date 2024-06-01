from rest_framework import serializers
from .models import *
from protection_certificate.models import ProtectionToolCertificate


class ProtectionToolCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectionToolCertificate
        fields = ['number', 'date_added']


class ProtectionToolFunctionSerializer(serializers.ModelSerializer):
    certificates = ProtectionToolCertificateSerializer(many=True, read_only=True, source='protectiontoolcertificate_set')
    class Meta:
        model = ProtectionToolFunction
        fields = ['id', 'title', 'symbol', 'certificates']


class BasicProtectionToolFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectionToolFunction
        fields = ['id', 'title', 'symbol']
