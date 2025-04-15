from abc import ABC, abstractmethod
from pathlib import Path
from filereaders import reader_dict, FileReader
from config import settings
from typing import Optional

class ReportBase(ABC):

    def __init__(self, file_paths: Optional[list[str]] = None) -> None:
        
        self.file_paths: list[str] = file_paths
        
        if not self.file_paths:
            self.file_paths: list[str] = []

        self.report: dict = dict()

    def change_file_paths(self, file_paths: Optional[list[str]]) -> None:
        self.file_paths = file_paths

    @abstractmethod
    def build_report(self) -> dict:
        """
        Создает и возвращает отчет в виде словаря
        """
        pass
        

    def save_report(self)->None:
        """
        Создает и сохраняет отчет в объекте
        """
        self.report = self.build_report()

    def print_report(self) -> None:
        """
        Печатает отчет
        """
        self.service_print_report(self.build_report())
        

    def print_report_current(self) -> None:
        """
        Печатает отчет, находящийся в объекте
        """
        self.service_print_report(self.report)

    def service_print_report(self, report: dict):

        if settings.report_service_column_name in report:
            service_line = report[settings.report_service_column_name]
            del report[settings.report_service_column_name]

        if settings.report_error_column_name in report:
            error_line = report[settings.report_error_column_name]
            del report[settings.report_error_column_name]

        if report:

            line = f"{'HANDLER':^{settings.report_handler_column_size}}"

            for column in settings.levels_set:
                line += "".join(f"{column:^{settings.report_levels_column_size}}")
            
            print(line)

            for handler, levels in report.items():
                line = f"{handler:^{settings.report_handler_column_size}}"
                for column in settings.levels_set:
                    if column in levels:
                        line += "".join(f"{levels[column]:^{settings.report_levels_column_size}}")
                    else:
                        line += "".join(f"{' ':^{settings.report_levels_column_size}}")

                print(line)

        print(service_line)
        for error in error_line:
            print(error)

    def get_report(self) -> dict:
        return self.report

    def get_file_type(self, file_path) -> None:
        return Path(file_path).suffix
    
    def get_file_reader(self, file_path) -> FileReader:
            file_type = self.get_file_type(file_path)

            for key, value in settings.extenstions_dict.items():
                if  file_type in value:
                    return reader_dict[key]
            return None
