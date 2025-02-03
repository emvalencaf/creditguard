from os import path
import logging

from config import ml_settings
from helpers.makedir import ensure_dir
from helpers.datetime_partition import get_datetime_partition, get_timestamp

def get_logging():
    """
    Configure a logging object
    :return: instance of logging
    """
    date_dir = get_datetime_partition()
    
    log_dir = f'{ml_settings.LOG_DIRECTORY}/{date_dir}'
    
    ensure_dir(directory=log_dir)

    timestamp = get_timestamp()

    logging.basicConfig(
        filename=path.join(log_dir, f'{timestamp}.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    return logging

ml_logging = get_logging()