# Generated by Django 5.0.6 on 2024-05-31 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protection_certificate', '0004_alter_protectiontoolcertificate_support_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='number',
            field=models.CharField(max_length=1024, verbose_name='№ сертификата'),
        ),
    ]