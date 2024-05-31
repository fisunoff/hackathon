from rest_framework import serializers
from .models import *
from protection_tool.serializers import BasicProtectionToolSerializer


class ProtectionToolCertificateSerializer(serializers.ModelSerializer):
    tool = BasicProtectionToolSerializer()

    class Meta:
        model = ProtectionToolCertificate
        fields = ['number', 'date_added', 'validity_period', 'tool', 'documents',
                  'certification_schema', 'laboratory', 'agency', 'applicant',
                  'requisites', 'support_period', 'functions']


class ProtectionToolCertificateDiffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectionToolCertificateDiff
        fields = [
            'reason',  # Тип изменения
            'number',  # № сертификата
            'date_added_old',  # Дата внесения в реестр
            'date_added_new',  # Дата внесения в реестр
            'validity_period_old',  # Срок действия сертификата
            'validity_period_new',  # Срок действия сертификата
            'tool_old',  # СЗИ
            'tool_new',  # СЗИ
            'documents_old',  # Наименования документов, требованиям которых соответствует средство
            'documents_new',  # Наименования документов, требованиям которых соответствует средство
            'certification_schema_old',  # Схема сертификации
            'certification_schema_new',  # Схема сертификации
            'laboratory_old',  # Испытательная лаборатория
            'laboratory_new',  # Испытательная лаборатория
            'agency_old',  # Орган по сертификации
            'agency_new',  # Орган по сертификации
            'applicant_old',  # Заявитель
            'applicant_new',  # Заявитель
            'requisites_old',  # Реквизиты заявителя (индекс, адрес, телефон)
            'requisites_new',  # Реквизиты заявителя (индекс, адрес, телефон)
            'support_period_old',  # Информация об окончании срока технической поддержки, полученная от заявителя
            'support_period_new'  # Информация об окончании срока технической поддержки, полученная от заявителя
        ]

