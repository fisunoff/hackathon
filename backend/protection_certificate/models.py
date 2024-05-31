from django.db import models

from utils.models import AuthoringModel

from protection_certificate import const


# Create your models here.
class ProtectionToolCertificate(AuthoringModel):
    number = models.CharField(max_length=1024, unique=True, verbose_name='№ сертификата')
    date_added = models.DateField(verbose_name='Дата внесения в реестр')
    validity_period = models.DateField(verbose_name='Срок действия сертификата')
    tool = models.ForeignKey(to='protection_tool.ProtectionTool', null=False, on_delete=models.CASCADE)
    documents = models.TextField(verbose_name='Наименования документов, требованиям которых соответствует средство')
    certification_schema = models.CharField(verbose_name='Схема сертификации', max_length=1024)
    laboratory = models.CharField(verbose_name='Испытательная лаборатория', max_length=1024)
    agency = models.CharField(verbose_name='Орган по сертификации', max_length=1024)
    applicant = models.CharField(verbose_name='Заявитель', max_length=1024)
    requisites = models.CharField(verbose_name='Реквизиты заявителя (индекс, адрес, телефон)', max_length=1024)
    support_period = models.DateField(
        verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя'
    )
    functions = models.ManyToManyField(to='protection_function.ProtectionToolFunction', verbose_name='Функции')

    class Meta:
        verbose_name = 'Сертификат СЗИ'


class ProtectionToolCertificateDiff(AuthoringModel):
    reason = models.IntegerField(verbose_name='Тип изменения', choices=const.reasons)
    number = models.CharField(max_length=1024, unique=True, verbose_name='№ сертификата')
    date_added_old = models.DateField(verbose_name='Дата внесения в реестр (старое)')
    date_added_new = models.DateField(verbose_name='Дата внесения в реестр (новое)')

    validity_period_old = models.DateField(verbose_name='Срок действия сертификата (старое)')
    validity_period_new = models.DateField(verbose_name='Срок действия сертификата (новое)')
    tool_old = models.CharField('СЗИ (старое)', max_length=1024)
    tool_new = models.CharField('СЗИ (новое)', max_length=1024)
    documents_old = models.TextField(verbose_name='Наименования документов, требованиям которых соответствует средство (старое)')
    documents_new = models.TextField(verbose_name='Наименования документов, требованиям которых соответствует средство (новое)')
    certification_schema_old = models.CharField(verbose_name='Схема сертификации (старое)', max_length=1024)
    certification_schema_new = models.CharField(verbose_name='Схема сертификации (новое)', max_length=1024)
    laboratory_old = models.CharField(verbose_name='Испытательная лаборатория (старое)', max_length=1024)
    laboratory_new = models.CharField(verbose_name='Испытательная лаборатория (новое)', max_length=1024)
    agency_old = models.CharField(verbose_name='Орган по сертификации (старое)', max_length=1024)
    agency_new = models.CharField(verbose_name='Орган по сертификации (новое)', max_length=1024)
    applicant_old = models.CharField(verbose_name='Заявитель (старое)', max_length=1024)
    applicant_new = models.CharField(verbose_name='Заявитель (новое)', max_length=1024)
    requisites_old = models.CharField(verbose_name='Реквизиты заявителя (индекс, адрес, телефон) (старое)', max_length=1024)
    requisites_new = models.CharField(verbose_name='Реквизиты заявителя (индекс, адрес, телефон) (новое)', max_length=1024)
    support_period_old = models.DateField(
        verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя (старое)'
    )
    support_period_new = models.DateField(
        verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя (новое)'
    )
    version = models.ForeignKey(to='updater.Version', on_delete=models.PROTECT, verbose_name='версия')

    class Meta:
        verbose_name = 'Обновление сертификата СЗИ'
