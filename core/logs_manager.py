from core import file_manager as fm
import logging

class LogsManager:
    def __init__(self):
        pass
    def create_log(self):
        log = fm.FileManager().get_path("logs") / "Support.log"
        pass


logging.basicConfig(level=logging.DEBUG)
logging.debug("Logs manager initialized.")
fm.FileManager().get_path("logs")
