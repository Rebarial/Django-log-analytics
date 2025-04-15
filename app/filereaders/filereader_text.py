from .filereader_base import FileReaderBase
from config import settings
import os
from pathlib import Path

class FileReaderText(FileReaderBase):

    @staticmethod
    def read_file(file_path: str) -> str:
        if os.path.exists(file_path):
            if Path(file_path).suffix in settings.extenstions_dict["text"]:
                with open(file_path, 'r', encoding='utf-8') as file:
                    return file.read()
            else:
                return ""
        else:
            return ""