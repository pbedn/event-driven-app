import time
from datetime import datetime

import schedule

from config import config
from logger import logger


def service_job():
    logger.info(f"Started job using SCHEDULE LIBRARY at {datetime.now()}")
    logger.info(f"Log file path: {config.log_file_path}")
    logger.info(f"Secret message: {config.secret}")


schedule.every().minute.do(service_job)


if __name__ == "__main__":
    logger.info("Starting Python Scheduler")
    while True:
        schedule.run_pending()
        time.sleep(1)
