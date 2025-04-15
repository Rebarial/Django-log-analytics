from argparse import ArgumentParser
from reports import report_dict


from filereaders.filereader_text import FileReaderText

def main() -> None:
    parser = ArgumentParser(description="Анализ логов Django-приложения.")
    parser.add_argument('log_files', nargs='+', help='Пути к логам')
    parser.add_argument('--report', type=str, help='Тип отчета (например, handlers)', required=True)

    args = parser.parse_args()

    if not args.report in report_dict:
        print(f"Ошибка: отчет '{args.report}' не поддерживается")
        return

    report = report_dict[args.report](args.log_files)
    report.print_report()

if __name__ == "__main__":
    main()