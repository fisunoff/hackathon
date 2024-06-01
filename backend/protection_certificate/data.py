from dataclasses import dataclass
from datetime import datetime

from utils.funcs import render_date


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

    def __eq__(self, other):
        return all((
            self.number == other.number,
            self.date_added == other.date_added,
            self.validity_period == other.validity_period,
            self.tool == other.tool,
            self.documents == other.documents,
            self.certification_schema == other.certification_schema,
            self.laboratory == other.laboratory,
            self.agency == other.agency,
            self.applicant == other.applicant,
            self.requisites == other.requisites,
            self.support_period == other.support_period,
            self.validity_period_infinity == other.validity_period_infinity,
            self.support_period_infinity == other.support_period_infinity,
            self.pause == other.pause,
        ))

    def get_diff(self, other):
        diff = ''
        if self.date_added != other.date_added:
            diff += f'Дата внесения в реестр: {self.date_added} → {other.date_added}\n'
        if render_date(self.validity_period, self.validity_period_infinity) != render_date(other.validity_period, other.validity_period_infinity):
            diff += (f'Срок действия сертификата: '
                     f'{render_date(self.validity_period, self.validity_period_infinity)} '
                     f'→ {render_date(other.validity_period, other.validity_period_infinity)}\n')
        if self.tool != other.tool:
            diff += f'СЗИ: {self.tool} → {other.tool}\n'
        if self.documents != other.documents:
            diff += f'Документы: {self.documents} → {other.documents}\n'
        if self.certification_schema != other.certification_schema:
            diff += f'Схема сертификации: {self.certification_schema} → {other.certification_schema}\n'
        if self.laboratory != other.laboratory:
            diff += f'Испытательная лаборатория: {self.laboratory} → {other.laboratory}\n'
        if self.agency != other.agency:
            diff += f'Орган по сертификации: {self.agency} → {other.agency}\n'
        if self.applicant != other.applicant:
            diff += f'Заявитель: {self.applicant} → {other.applicant}\n'
        if self.requisites != other.requisites:
            diff += f'Реквизиты заявителя: {self.requisites} → {other.requisites}\n'

        if render_date(self.support_period, self.support_period_infinity) != render_date(other.support_period, other.support_period_infinity):
            diff += (f'Срок действия сертификата: '
                     f'{render_date(self.support_period, self.support_period_infinity)} '
                     f'→ {render_date(other.support_period, other.support_period_infinity)}\n')
        if self.pause and not other.pause:
            diff += 'Действие сертификата больше не приостановлено\n'
        if not self.pause and other.pause:
            diff += 'Действие сертификата приостановлено\n'
        return diff.strip('\n')
