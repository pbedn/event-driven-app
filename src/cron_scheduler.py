import argparse
import time
from datetime import datetime

from logger import logger

from config import config


print(f"Starting CronScheduler")
print(datetime.now())
print(config.secret)
print(config.log_file_path)
print(config.cron_log_path)
print()

# def service_job():
#     logger.info(f"Started job using SCHEDULE LIBRARY at {datetime.now()}")
#     logger.info(f"Log file path: {config.log_file_path}")
#     logger.info(f"Secret message: {config.secret}")
#
#
# def get_argument_parser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--service-job', action='store_true')
#     return parser
#
#
# if __name__ == '__main__':
#     logger.info("Starting cron scheduler")
#     argument_parser = get_argument_parser()
#     args = argument_parser.parse_args()
#
#     if args.service_job:
#         service_job()
