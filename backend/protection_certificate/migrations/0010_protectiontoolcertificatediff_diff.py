# Generated by Django 5.0.6 on 2024-05-31 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protection_certificate', '0009_protectiontoolcertificatediff_support_period_infinity_new_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='protectiontoolcertificatediff',
            name='diff',
            field=models.TextField(blank=True, null=True, verbose_name='Отчет по разнице'),
        ),
    ]
