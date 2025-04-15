import os
import sys
from argparse import ArgumentParser

sys.path = ['', '..'] + sys.path[1:]
sys.path.append(os.getcwd()+"\\app")
sys.path.append(os.getcwd()+"/app")

from filereaders.filereader_text import FileReaderText

if __name__ == "__main__":
    parser = ArgumentParser(description="Анализ логов Django-приложения.")
    parser.add_argument('log_files', nargs='+', help='Пути к логам')
    parser.add_argument('--report', type=str, help='Тип отчета (например, handlers)')

    args = parser.parse_args()

    print(args)
