from rest_framework import serializers
from .models import *


class ProtectionToolFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectionToolFunction
        fields = ['id', 'title', 'symbol']
