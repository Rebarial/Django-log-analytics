import re

from .report_base import ReportBase
from config import settings

class ReportHandlers(ReportBase):

    def build_report(self) -> dict:
        error = self.get_error()
        if error:
            return error

        logs = self.file_reader.read_file(self.file_path)

        if not logs:
            return {settings.report_service_column_name: f"Ошибка: Файл '{self.file_path}' не существует или он пуст!"}

        result = {}

        levels_set = set()

        total_requests = 0

        handler_regul = r'(/[^ ]+/?)'

        last_handler = None

        level_regul = r'.\d{3}\s+(\w+)\s+(django)'

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

            levels_set.add(level)

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
