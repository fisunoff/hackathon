from django.db import models

from utils.models import AuthoringModel


class ProtectionToolFunction(AuthoringModel):
    title = models.CharField(max_length=1024, verbose_name='Наименование')
