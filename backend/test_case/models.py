from django.db import models


class TestCase(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', null=False, blank=False)
    param1 = models.IntegerField(verbose_name='Параметр 1', null=False, blank=False)
    param2 = models.IntegerField(verbose_name='Параметр 2', null=False, blank=False)

    class Meta:
        verbose_name = 'Тестовый сценарий'

    @property
    def param3(self) -> int:
        return self.param1 + self.param2
