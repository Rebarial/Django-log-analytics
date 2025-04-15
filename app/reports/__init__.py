__all__= (
    "report_dict",
)

from .report_base import ReportBase
from .report_handlers import ReportHandlers


report_dict: dict[ReportBase] = {
    "handlers": ReportHandlers, 
}