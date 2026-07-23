from pathlib import Path
from datetime import datetime


def make_log_dir(year, month):
    logs_path = Path("logs").mkdir(parents=True, exist_ok=True)


current_year =  datetime.now().strftime("%y")
current_month =  datetime.now().strftime("%m")

make_log_dir(current_year, current_month)
