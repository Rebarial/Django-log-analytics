import re

from .report_base import ReportBase
from config import settings

class ReportHandlers(ReportBase):

    def build_report(self) -> dict:
        
        result = {}
        total_requests = 0

        handler_regul = r'(/[^ ]+/?)'
        level_regul = r'.\d{3}\s+(\w+)\s+(django)'

        last_handler = None
        
        result[settings.report_error_column_name] = []

        for file_path in self.file_paths:
            filereader = self.get_file_reader(file_path)
            
            if not filereader:
                result[settings.report_error_column_name].append(f"Ошибка: Расширение файла '{file_path}' не поддерживается!")
                continue

            logs = filereader.read_file(file_path)

            if not logs:
                result[settings.report_error_column_name].append(f"Ошибка: Файл '{file_path}' не существует или он пуст!")
                continue


            for line in logs.strip().split('\n'):

                handler = re.search(handler_regul, line)

                if handler:
                    last_handler = handler.group(1)

                if not last_handler:
                    continue

                level = re.search(level_regul, line)
                    
                if not level:
                    continue

                level = level.group(1)

                total_requests += 1

                if last_handler in result:

                    if level in result[last_handler]:
                        result[last_handler][level] += 1
                    else:
                        result[last_handler][level] = 1       
                else:
                    result[last_handler] = {level: 1}

        result[settings.report_service_column_name] = f"Total requests: {total_requests}"

        return dict(sorted(result.items()))
