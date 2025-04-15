from abc import ABC, abstractmethod

class FileReaderBase(ABC):

    @staticmethod
    def read_file(file_path: str):
        print(file_path)

    