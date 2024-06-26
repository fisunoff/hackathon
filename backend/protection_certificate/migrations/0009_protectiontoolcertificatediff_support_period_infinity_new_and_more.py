# Generated by Django 5.0.6 on 2024-05-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protection_certificate', '0008_alter_protectiontoolcertificate_validity_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='protectiontoolcertificatediff',
            name='support_period_infinity_new',
            field=models.BooleanField(default=False, verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя - бессрочно (новое)'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificatediff',
            name='support_period_infinity_old',
            field=models.BooleanField(default=False, verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя - бессрочно (старое)'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificatediff',
            name='validity_period_infinity_new',
            field=models.BooleanField(default=False, verbose_name='Срок действия - бессрочно (новое)'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificatediff',
            name='validity_period_infinity_old',
            field=models.BooleanField(default=False, verbose_name='Срок действия - бессрочно (старое)'),
        ),
    ]
