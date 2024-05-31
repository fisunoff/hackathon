# Generated by Django 5.0.6 on 2024-05-31 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protection_certificate', '0006_protectiontoolcertificate_pause_and_more'),
        ('protection_function', '0001_initial'),
        ('protection_tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='protectiontoolcertificate',
            name='support_period_infinity',
            field=models.BooleanField(default=False, verbose_name='Информация об окончании срока технической поддержки, полученная от заявителя - бессрочно'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificate',
            name='validity_period_infinity',
            field=models.BooleanField(default=False, verbose_name='Срок действия - бессрочно'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificate',
            name='functions',
            field=models.ManyToManyField(blank=True, to='protection_function.protectiontoolfunction', verbose_name='Функции'),
        ),
        migrations.AlterField(
            model_name='protectiontoolcertificate',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='protection_tool.protectiontool', verbose_name='Наименование средств'),
        ),
    ]
