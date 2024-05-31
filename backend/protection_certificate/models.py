from django.db import models

from protection_certificate.data import ProtectionToolCertificateData
from utils.models import AuthoringModel

from . import const


# Create your models here.
class ProtectionToolCertificate(AuthoringModel):
    number = models.CharField(max_length=1024, unique=True, verbose_name='№ сертификата')
    date_added = models.DateField(verbose_name='Дата внесения в реестр')
    validity_period = models.DateField(verbose_name='Срок действия сертификата', null=True)
    validity_period_infinity = models.BooleanField(verbose_name='Срок действия - бессрочно', default=False)
    tool = models.ForeignKey(
        to='protection_tool.ProtectionTool',
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Наименование средств',
        related_name='certificates'
    )
    documents = models.TextField(verbose_name='Наименования документов, требованиям которых соответствует средство')
    certification_schema = models.CharField(verbose_name='Схема сертификации', max_length=1024)
    laboratory = models.CharField(verbose_name='Испытательная лаборатория', max_length=1024)
    agency = models.CharField(verbose_name='Орган по сертификации', max_length=1024)
    applicant = models.CharField(verbose_name='Заявитель', max_length=1024)
    requisites = models.CharField(verbose_name='Реквизиты заявителя (индекс, адрес, телефон)', max_length=1024)
    support_period = models.DateField(
        verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя',
        null=True,
    )
    support_period_infinity = models.BooleanField(
        verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя - бессрочно',
        default=False,
    )
    # TODO: дата приостановки
    pause = models.BooleanField(verbose_name='Действие сертификата соответствия приостановлено', default=False)
    functions = models.ManyToManyField(
        to='protection_function.ProtectionToolFunction',
        verbose_name='Функции',
        blank=True
    )

    class Meta:
        verbose_name = 'Сертификат СЗИ'

    @classmethod
    def get_caches(cls):
        return {
            row.number: ProtectionToolCertificateData(
                row.number,
                row.date_added,
                row.validity_period,
                row.validity_period_infinity,
                row.tool.title,
                row.documents,
                row.certification_schema,
                row.laboratory,
                row.agency,
                row.applicant,
                row.requisites,
                row.support_period,
                row.support_period_infinity,
                row.pause,
                row.id
            )
            for row in cls.objects.all()
        }

    def __str__(self):
        return self.number


class ProtectionToolCertificateDiff(AuthoringModel):
    reason = models.IntegerField(verbose_name='Тип изменения', choices=const.reasons)
    number = models.CharField(max_length=1024, verbose_name='№ сертификата')
    date_added_old = models.DateField(verbose_name='Дата внесения в реестр (старое)', null=True)
    date_added_new = models.DateField(verbose_name='Дата внесения в реестр (новое)', null=True)

    validity_period_old = models.DateField(verbose_name='Срок действия сертификата (старое)', null=True)
    validity_period_new = models.DateField(verbose_name='Срок действия сертификата (новое)', null=True)
    tool_old = models.CharField('СЗИ (старое)', max_length=1024, null=True)
    tool_new = models.CharField('СЗИ (новое)', max_length=1024, null=True)
    documents_old = models.TextField(verbose_name='Наименования документов, требованиям которых соответствует средство (старое)', null=True)
    documents_new = models.TextField(verbose_name='Наименования документов, требованиям которых соответствует средство (новое)', null=True)
    certification_schema_old = models.CharField(verbose_name='Схема сертификации (старое)', max_length=1024, null=True)
    certification_schema_new = models.CharField(verbose_name='Схема сертификации (новое)', max_length=1024, null=True)
    laboratory_old = models.CharField(verbose_name='Испытательная лаборатория (старое)', max_length=1024, null=True)
    laboratory_new = models.CharField(verbose_name='Испытательная лаборатория (новое)', max_length=1024, null=True)
    agency_old = models.CharField(verbose_name='Орган по сертификации (старое)', max_length=1024, null=True)
    agency_new = models.CharField(verbose_name='Орган по сертификации (новое)', max_length=1024, null=True)
    applicant_old = models.CharField(verbose_name='Заявитель (старое)', max_length=1024, null=True)
    applicant_new = models.CharField(verbose_name='Заявитель (новое)', max_length=1024, null=True)
    requisites_old = models.CharField(verbose_name='Реквизиты заявителя (индекс, адрес, телефон) (старое)', max_length=1024, null=True)
    requisites_new = models.CharField(verbose_name='Реквизиты заявителя (индекс, адрес, телефон) (новое)', max_length=1024, null=True)
    support_period_old = models.DateField(
        verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя (старое)',
        null = True
    )
    support_period_new = models.DateField(
        verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя (новое)',
        null=True
    )
    pause_old = models.BooleanField(verbose_name='Действие сертификата соответствия приостановлено (старое)', default=False)
    pause_new = models.BooleanField(verbose_name='Действие сертификата соответствия приостановлено (новое)', default=False)
    version = models.ForeignKey(to='updater.Version', on_delete=models.PROTECT, verbose_name='версия')

    class Meta:
        verbose_name = 'Обновление сертификата СЗИ'

    @classmethod
    def create_from_data(cls, old_row, now, version_id):
        if old_row.number:
            reason = const.EDITED
        else:
            reason = const.ADDED
        cls.objects.create(
                reason=reason,
                number=now.number,
                date_added_old=old_row.date_added,
                date_added_new=now.date_added,
                validity_period_old=old_row.validity_period,
                validity_period_new=now.validity_period,
                tool_old=old_row.tool,
                tool_new=now.tool,
                documents_old=old_row.documents,
                documents_new=now.documents,
                certification_schema_old=old_row.certification_schema,
                certification_schema_new=now.certification_schema,
                laboratory_old=old_row.laboratory,
                laboratory_new=now.laboratory,
                agency_old=old_row.agency,
                agency_new=now.agency,
                applicant_old=old_row.applicant,
                applicant_new=now.applicant,
                requisites_old=old_row.requisites,
                requisites_new=now.requisites,
                support_period_old=old_row.support_period,
                support_period_new=now.support_period,
                pause_old=old_row.pause,
                pause_new=now.pause,
                version_id=version_id,
            )
