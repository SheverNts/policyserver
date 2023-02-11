import logging

log_formats = {
    "default": "{'time':'%(asctime)s', 'name': '%(name)s', \
    'level': '%(levelname)s', 'message': '%(message)s'}",
    "debug": "{'time':'%(asctime)s', 'name': '%(name)s', \
    'level': '%(levelname)s', 'message': '%(message)s'}",
}

log_levels = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "error": logging.ERROR,
    "warn": logging.WARN,
}


class Logs():
    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.stream_handler = logging.StreamHandler()

    def set_level(self, log_level):
        log_level = log_level.lower()
        self.logger.setLevel(log_levels.get(log_level))
        log_format = logging.Formatter(
            log_formats.get(log_level, log_formats.get('default'))
        )
        self.stream_handler.setFormatter(log_format)
        self.logger.addHandler(self.stream_handler)