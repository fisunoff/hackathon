from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.models import TimestampedModel, AuthoringModel


class Profile(TimestampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=50, blank=False, null=True)
    surname = models.CharField("Фамилия", max_length=50, blank=False, null=True)
    patronymic = models.CharField("Отчество", max_length=50, blank=True, null=True)
    bio = models.TextField("Описание профиля", max_length=500, blank=True, null=True)
    post = models.CharField(verbose_name="Должность", max_length=200, blank=True, null=True)
    manager = models.BooleanField(verbose_name='Менеджер', default=False)
    notify_me = models.BooleanField(verbose_name='Получать уведомления', default=True)

    def __str__(self):
        return f"{self.surname} {self.name}{' ' + self.patronymic if self.patronymic else ''}"

    @property
    def is_manager(self):
        return self.manager or self.user.is_superuser

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
