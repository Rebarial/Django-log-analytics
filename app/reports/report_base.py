from abc import ABC, abstractmethod

class ReportBase(ABC):

    name: str

    @abstractmethod
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    @abstractmethod
     def report(self):
        "generate report"
        pass

