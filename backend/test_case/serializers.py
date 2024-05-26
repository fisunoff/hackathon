from rest_framework import serializers

from .models import TestCase


class TestCaseSerializer(serializers.ModelSerializer):
    param3 = serializers.ReadOnlyField()

    class Meta:
        model = TestCase
        fields = ['name', 'param1', 'param2', 'param3']
