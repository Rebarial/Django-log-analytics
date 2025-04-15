from argparse import ArgumentParser
from reports import report_dict


from filereaders.filereader_text import FileReaderText

def main() -> None:
    parser = ArgumentParser(description="Анализ логов Django-приложения.")
    parser.add_argument('log_files', nargs='+', help='Пути к логам')
    parser.add_argument('--report', type=str, help='Тип отчета (например, handlers)')

    args = parser.parse_args()

    for log in args.log_files:
        report = report_dict[args.report](log)
        report.print_report()
        print()

if __name__ == "__main__":
    main()