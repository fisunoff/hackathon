from utils.models import AuthoringModel


class Version(AuthoringModel):
    class Meta:
        verbose_name = 'Обновление'

    def __str__(self):
        return self.created
