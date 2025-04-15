__all__= (
    "reader_dict",
    "FileReader",
)

from .filereader_base import FileReaderBase as FileReader
from .filereader_text import FileReaderText


reader_dict = {
    "text": FileReaderText, 
}