from django.db import models

from utils.models import AuthoringModel


# Create your models here.
class ProtectionToolCertificate(AuthoringModel):
    number = models.CharField(max_length=1024, unique=True, verbose_name='№ сертификата')
    date_added = models.DateField(verbose_name='Дата внесения в реестр')
    validity_period = models.DateField(verbose_name='Срок действия сертификата')
    # TODO: посмотреть, может у одного сертификата может быть несколько СЗИ
    tool = models.ForeignKey(to='protection_tool.ProtectionTool', null=False, on_delete=models.CASCADE)
    # TODO: возможно, вынести в модель
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
