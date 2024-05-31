# Generated by Django 5.0.6 on 2024-05-31 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protection_certificate', '0005_alter_protectiontoolcertificatediff_number'),
        ('protection_tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='protectiontoolcertificate',
            name='pause',
            field=models.BooleanField(default=False, verbose_name='Действие сертификата соответствия приостановлено'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificatediff',
            name='pause_new',
            field=models.BooleanField(default=False, verbose_name='Действие сертификата соответствия приостановлено (новое)'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificatediff',
            name='pause_old',
            field=models.BooleanField(default=False, verbose_name='Действие сертификата соответствия приостановлено (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificate',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protection_tool.protectiontool', verbose_name='Наименование средств'),
        ),
    ]
