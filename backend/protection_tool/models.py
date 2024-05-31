from django.db import models

from utils.models import TimestampedModel


# Create your models here.
class ProtectionTool(TimestampedModel):
    title = models.CharField(max_length=1024, unique=True, verbose_name='Наименование средства')
