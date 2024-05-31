import os
from datetime import datetime

import numpy as np

from protection_certificate.data import ProtectionToolCertificateData
from protection_certificate.models import ProtectionToolCertificateDiff, ProtectionToolCertificate
from protection_tool.models import ProtectionTool
from updater.const import IN_PROGRESS, DONE
from updater.models import Version


def get_caches():
    from protection_certificate.models import ProtectionToolCertificate
    return ProtectionToolCertificate.get_caches()


def process_data(data, version_id):
    cache = get_caches()
    protection_tool_cache = ProtectionTool.get_caches()
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.backend.settings')
    django.setup()
    version = Version.objects.get(id=version_id)
    version.status = IN_PROGRESS
    version.save()
    print('processing')
    for row in data.values:
        title = str(row[0])
        now = ProtectionToolCertificateData(
            *(str(i) for i in row),
        )

        now.date_added = datetime.strptime(now.date_added, "%d.%m.%Y").date()

        # region validity_period
        if str(now.validity_period).lower() == 'бессрочно':
            now.validity_period = None
            now.validity_period_infinity = True
        elif str(now.validity_period).lower().startswith('действие сертификата соответствия приостановлено'):
            now.validity_period = None
            now.pause = True
        else:
            now.validity_period = datetime.strptime(now.validity_period, "%d.%m.%Y").date()
        # endregion validity_period

        if str(now.support_period) == str(np.nan) or now.support_period is None:
            now.support_period = None
        elif str(now.support_period).lower() == 'бессрочно':
            now.support_period = None
            now.support_period_infinity = True
        else:
            now.support_period = datetime.strptime(now.support_period, "%d.%m.%Y").date()

        if now.tool in protection_tool_cache:
            tool_id = protection_tool_cache[now.tool]
        else:
            tool = ProtectionTool.objects.create(title=now.tool)
            tool_id = tool.id
            protection_tool_cache[now.tool] = tool_id

        if title in cache:
            old_row = cache[title]  # type: ProtectionToolCertificateData
            if old_row == now:
                continue  # не поменялось
            ProtectionToolCertificateDiff.create_from_data(old_row, now, version_id)

            ProtectionToolCertificate.objects.update_or_create(
                id=cache[now.number].id,
                defaults=dict(
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
            )
        else:
            ProtectionToolCertificateDiff.create_from_data(ProtectionToolCertificateData(), now, version_id)
            ProtectionToolCertificate.objects.create(
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
    version.status = DONE
    version.save()
