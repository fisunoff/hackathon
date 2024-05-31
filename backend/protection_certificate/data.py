from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProtectionToolCertificateData:
    number: str = None
    date_added: datetime.date = None
    validity_period: datetime.date = None
    tool: str = None
    documents: str = None
    certification_schema: str = None
    laboratory: str = None
    agency: str = None
    applicant: str = None
    requisites: str = None
    support_period: datetime.date = None
    validity_period_infinity: bool = False
    support_period_infinity: bool = False
    pause: bool = False
    id: int = None
