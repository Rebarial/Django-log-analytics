from filereader_base import FileReaderBase

class FileReaderText(FileReaderBase):

    @property    
    def name():
        return f"{__name__}"