import json
import logging
import sys

# create handler
handler = logging.StreamHandler(sys.stdout)

# set log level
handler.setLevel(logging.DEBUG)


# create a json formatter
class JsonFormatter(logging.Formatter):
    def format(self, record):
        record = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.filename,
        }
        return json.dumps(record)


# assign a formatter to the handler
handler.setFormatter(JsonFormatter())

# set root logger config
logging.root.setLevel(logging.DEBUG)
logging.root.addHandler(handler)

# set log level for supporting libs
logging.getLogger("requests").setLevel(logging.INFO)


# get logger based on module
def get_logger(module: str):
    logger = logging.getLogger(module)
    return logger
