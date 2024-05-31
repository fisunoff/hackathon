from django.db import models

from utils.models import TimestampedModel


# Create your models here.
class ProtectionTool(TimestampedModel):
    title = models.CharField(max_length=1024, unique=True, verbose_name='Наименование средства')

    class Meta:
        verbose_name = 'Средство защиты информации'

    def __str__(self):
        return self.title

    @classmethod
    def get_caches(cls):
        return {
            title: pk
            for (title, pk) in cls.objects.values_list('title', 'pk')
        }
