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
def test_report_handlers_set_file_reader(filepath, result):
    report_handlers = ReportHandlers(file_path=filepath)
    assert report_handlers.file_reader == result


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
def test_report_handlers_change_file_path(filepath, result):
    report_handlers = ReportHandlers(file_path="text.log")
    report_handlers.change_file_path(file_path=filepath)
    assert report_handlers.file_reader == result


def test_report_handlers_get_error_no_reader():
    report_handlers = ReportHandlers(file_path="text.unknown")
    error = report_handlers.get_error()
    assert error == {settings.report_service_column_name: "Ошибка: Расширение файла 'text.unknown' не поддерживается!"}

def test_report_handlers_build_report_empty_file():
    report_handlers = ReportHandlers("unknown.txt")
    report = report_handlers.build_report()
    assert report == {settings.report_service_column_name: "Ошибка: Файл 'unknown.txt' не существует или он пуст!"}

def test_report_handlers_build_report_empty_file_path():
    report_handlers = ReportHandlers("")
    report = report_handlers.build_report()
    assert report == {settings.report_service_column_name: "Ошибка: не указан путь к файлу"}

def test_report_handlers_build_report_success():

    report_handlers = ReportHandlers("app/tests/logs/app1.log")

    expected_result = {
        "/api/v1/reviews/": {"INFO": 1},
        settings.report_service_column_name: "Total requests: 1"
    }
    
    assert expected_result == report_handlers.build_report()