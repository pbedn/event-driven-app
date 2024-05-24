import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Config:
    # secret is read only from .env file
    secret = os.getenv('SECRET')

    # log path might be from .env or system env
    log_file_path = os.getenv('LOG_FILE_PATH')

    # cron path is only used inside docker container
    cron_log_path = '/tmp/cron_log'


config = Config()
