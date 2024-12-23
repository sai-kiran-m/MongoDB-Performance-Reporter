from abc import ABC, abstractmethod


class ReportBase(ABC):

    @abstractmethod
    def report(self):
        pass
