from abc import ABC, abstractmethod

from reports.report_base import ReportBase


class ReportFactoryBase(ABC):
    @abstractmethod
    def create_report(self) -> ReportBase:
        pass
