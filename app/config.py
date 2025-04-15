class Config():

    def __init__(
            self,
            extenstions_dict: dict =
            {
                "text": [".txt", ".log"]
            },
            levels_set: set = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"},
            report_levels_column_size: int = 10,
            report_handler_column_size: int = 30,
            report_service_column_name: str = "!service"
    ):
        self.extenstions_dict: dict = extenstions_dict
        self.levels_set: set = levels_set
        self.report_levels_column_size: int = report_levels_column_size
        self.report_handler_column_size: int = report_handler_column_size
        self.report_service_column_name: str = report_service_column_name


settings = Config()