import os
from datetime import datetime

from protection_certificate.data import ProtectionToolCertificateData
from protection_certificate.models import ProtectionToolCertificateDiff, ProtectionToolCertificate
from protection_tool.models import ProtectionTool
from updater.models import Version


def get_caches():
    from protection_certificate.models import ProtectionToolCertificate
    return ProtectionToolCertificate.get_caches()


def process_data(data):
    cache = get_caches()
    protection_tool_cache = ProtectionTool.get_caches()
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.backend.settings')
    django.setup()
    version = Version.objects.create()
    for row in data.values:
        title = row[0]
        now = ProtectionToolCertificateData(
            *row,
        )
        now.date_added = datetime.strptime(now.date_added, "%d.%m.%Y").date()
        now.validity_period = datetime.strptime(now.validity_period, "%d.%m.%Y").date()
        now.support_period = datetime.strptime(now.support_period, "%d.%m.%Y").date()

        if now.tool in protection_tool_cache:
            tool_id = protection_tool_cache[now.tool]
        else:
            tool = ProtectionTool.objects.create(title=now.tool)
            tool_id = tool.id

        if title in cache:
            old_row = cache[title]  # type: ProtectionToolCertificateData
            if old_row == now:
                continue  # не поменялось
            ProtectionToolCertificateDiff.create_from_data(old_row, now, version.id)

            certificate = ProtectionToolCertificate.objects.get(pk=cache[now.number])
            certificate.update(
                date_added=now.date_added,
                validity_period=now.validity_period,
                tool_id=tool_id,
                documents=now.documents,
                certification_schema=now.certification_schema,
                laboratory=now.laboratory,
                agency=now.agency,
                applicant=now.applicant,
                requisites=now.requisites,
                support_period=now.support_period,
            )
        else:
            ProtectionToolCertificateDiff.create_from_data(ProtectionToolCertificateData(), now, version.id)
            certificate = ProtectionToolCertificate.objects.create(
                number=now.number,
                date_added=now.date_added,
                validity_period=now.validity_period,
                tool_id=tool_id,
                documents=now.documents,
                certification_schema=now.certification_schema,
                laboratory=now.laboratory,
                agency=now.agency,
                applicant=now.applicant,
                requisites=now.requisites,
                support_period=now.support_period,
            )
