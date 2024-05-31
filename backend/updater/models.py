from django.db import models

from utils.models import AuthoringModel
from . import const


class Version(AuthoringModel):
    status = models.IntegerField(verbose_name='Статус', choices=const.STATUSES, default=const.CREATED)

    class Meta:
        verbose_name = 'Обновление'

    def __str__(self):
        return str(self.created)

    @classmethod
    def get_last_update(cls):
        return cls.objects.order_by('id').last()
