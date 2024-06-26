# Generated by Django 5.0.6 on 2024-05-31 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extended_user', '0001_initial'),
        ('protection_certificate', '0001_initial'),
        ('protection_function', '0001_initial'),
        ('protection_tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='protectiontoolcertificate',
            name='functions',
            field=models.ManyToManyField(to='protection_function.protectiontoolfunction', verbose_name='Функции'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificate',
            name='last_editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_by_editors', to='extended_user.profile', verbose_name='Автор последних изменений'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificate',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protection_tool.protectiontool'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificatediff',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_by_author', to='extended_user.profile', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='protectiontoolcertificatediff',
            name='last_editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_by_editors', to='extended_user.profile', verbose_name='Автор последних изменений'),
        ),
    ]
