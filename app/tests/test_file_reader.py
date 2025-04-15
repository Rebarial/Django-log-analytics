from filereaders import FileReaderText

def test_file_reader_text_read_file_exists():

    result = """2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]"""

    assert result == FileReaderText.read_file("app/tests/logs/app1.log")

def test_file_reader_text_read_file_not_exists():
        assert FileReaderText.read_file("unknown.txt") == ""

def test_file_reader_excel_file():
    assert "" == FileReaderText.read_file("app/tests/logs/test.xlsx")