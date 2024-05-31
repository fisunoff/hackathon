# Generated by Django 5.0.6 on 2024-05-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protection_certificate', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protectiontoolcertificate',
            name='support_period',
            field=models.DateField(null=True, verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='agency_new',
            field=models.CharField(max_length=1024, null=True, verbose_name='Орган по сертификации (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='agency_old',
            field=models.CharField(max_length=1024, null=True, verbose_name='Орган по сертификации (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='applicant_new',
            field=models.CharField(max_length=1024, null=True, verbose_name='Заявитель (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='applicant_old',
            field=models.CharField(max_length=1024, null=True, verbose_name='Заявитель (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='certification_schema_new',
            field=models.CharField(max_length=1024, null=True, verbose_name='Схема сертификации (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='certification_schema_old',
            field=models.CharField(max_length=1024, null=True, verbose_name='Схема сертификации (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='date_added_new',
            field=models.DateField(null=True, verbose_name='Дата внесения в реестр (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='date_added_old',
            field=models.DateField(null=True, verbose_name='Дата внесения в реестр (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='documents_new',
            field=models.TextField(null=True, verbose_name='Наименования документов, требованиям которых соответствует средство (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='documents_old',
            field=models.TextField(null=True, verbose_name='Наименования документов, требованиям которых соответствует средство (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='laboratory_new',
            field=models.CharField(max_length=1024, null=True, verbose_name='Испытательная лаборатория (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='laboratory_old',
            field=models.CharField(max_length=1024, null=True, verbose_name='Испытательная лаборатория (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='requisites_new',
            field=models.CharField(max_length=1024, null=True, verbose_name='Реквизиты заявителя (индекс, адрес, телефон) (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='requisites_old',
            field=models.CharField(max_length=1024, null=True, verbose_name='Реквизиты заявителя (индекс, адрес, телефон) (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='support_period_new',
            field=models.DateField(null=True, verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='support_period_old',
            field=models.DateField(null=True, verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='tool_new',
            field=models.CharField(max_length=1024, null=True, verbose_name='СЗИ (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='tool_old',
            field=models.CharField(max_length=1024, null=True, verbose_name='СЗИ (старое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='validity_period_new',
            field=models.DateField(null=True, verbose_name='Срок действия сертификата (новое)'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificatediff',
            name='validity_period_old',
            field=models.DateField(null=True, verbose_name='Срок действия сертификата (старое)'),
        ),
    ]
