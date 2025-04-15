from reports import ReportHandlers
from filereaders import FileReaderText
from config import settings
import pytest

@pytest.mark.parametrize("filepath, result", 
                         [
                             ("test.txt",FileReaderText),
                             ("test.unknown", None),
                             ("test.xlsx", None),
                             ("test.", None),
                             ("test", None),
                             ("", None),
                         ]    
                         )
def test_report_handlers_get_file_reader(filepath, result):
    report_handlers = ReportHandlers()
    assert report_handlers.get_file_reader(filepath) == result


def test_report_handlers_change_file_path_success():
    report_handlers = ReportHandlers(file_paths=["text.log"])
    report_handlers.change_file_paths(file_paths=["text1.log"])
    assert report_handlers.file_paths == ["text1.log"]

def test_report_handlers_build_report_empty_file():
    report_handlers = ReportHandlers(["unknown.txt"])
    report = report_handlers.build_report()
    assert report == {settings.report_error_column_name: ["Ошибка: Файл 'unknown.txt' не существует или он пуст!"],
        settings.report_service_column_name: 'Total requests: 0'}

def test_report_handlers_build_report_empty_file_path():
    report_handlers = ReportHandlers([""])
    report = report_handlers.build_report()
    assert report == {settings.report_error_column_name: ["Ошибка: Расширение файла '' не поддерживается!"],
                      settings.report_service_column_name: 'Total requests: 0'}

def test_report_handlers_build_report_success():

    report_handlers = ReportHandlers(["app/tests/logs/app1.log"])

    expected_result = {
        "!error": [],
        "/api/v1/reviews/": {"INFO": 1},
        settings.report_service_column_name: "Total requests: 1"
    }
    
    assert expected_result == report_handlers.build_report()