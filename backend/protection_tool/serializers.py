from rest_framework import serializers
from .models import ProtectionTool


class ProtectionToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectionTool
        fields = ['title']
