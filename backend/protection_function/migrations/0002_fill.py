from django.db import migrations
from django.db.migrations import RunPython

functions = (
    ('МЭ', 'Межсетевое экранирование'),
    ('IDS', 'Система обнаружения вторжения'),
    ('САВЗ', 'Средство антивирусной защиты'),
    ('СКД', 'Система контроля доступа'),
    ('СКЗИ', 'Средство криптографической защиты информации'),
    ('СОВ', 'Система обеспечения целостности'),
    ('СР', 'Средство резервного копирования'),
    ('САЗ', 'Система анализа защищенности'),
    ('САЗИ', 'Система анализа и защиты информации'),
    ('СПО', 'Система предотвращения потери информации'),
    ('СОВ', 'Средство обнаружения вторжения'),
    ('ПСЗ', 'Программные средства защиты'),
)


def _fill_functions(apps, schema_editor):
    ProtectionToolFunction = apps.get_model('protection_function', 'ProtectionToolFunction')
    for (symbol, title) in functions:
        ProtectionToolFunction.objects.create(
            symbol=symbol,
            title=title
        )


def _functions(apps, schema_editor):
    ProtectionToolFunction = apps.get_model('protection_function', 'ProtectionToolFunction')
    ProtectionToolFunction.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('protection_function', '0001_initial'),
    ]

    operations = [
        RunPython(_fill_functions, reverse_code=_functions, atomic=False),
    ]
