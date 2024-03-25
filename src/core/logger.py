import orjson as json
import logging
import os
from datetime import datetime
from logging import Formatter, Logger
from logging.handlers import RotatingFileHandler
from .config import log_settings


class JsonFormatter(Formatter):
    def __init__(self) -> None:
        super(JsonFormatter, self).__init__()

    def format(self, record: logging.LogRecord):
        formatted_message = "%(levelname)s %(name)s %(asctime)-4s: %(message)s" % {
            "name": record.module,
            "asctime": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "levelname": record.levelname,
            "message": record.getMessage(),
        }

        json_record = {"message": formatted_message}

        if "req" in record.__dict__:
            json_record["req"] = record.__dict__["req"]
        if "res" in record.__dict__:
            json_record["res"] = record.__dict__["res"]
        if record.levelno == logging.ERROR and record.exc_info:
            json_record["err"] = self.formatException(record.exc_info)
        return json.dumps(json_record).decode("utf-8")


if not os.path.exists(log_settings.dir):
    os.makedirs(log_settings.dir)
log_path = os.path.join(log_settings.dir, log_settings.file)

logger: Logger = logging.root
file_handler = RotatingFileHandler(
    filename=log_path,
    maxBytes=log_settings.size,
    backupCount=log_settings.backup_num,
)
file_handler.setFormatter(JsonFormatter())

logger.handlers = [file_handler]

logger.setLevel(logging.INFO)
