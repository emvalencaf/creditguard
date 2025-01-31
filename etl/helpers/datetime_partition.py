from datetime import datetime

def get_datetime_partition():
    """
    Get a datetime partition directory
    
    :return: string with datetime partition (ex: yyyy/mm/dd)
    """
    now = datetime.now()
    
    return f"{now.year}/{now.month}/{now.day}"

def get_timestamp():
    """
    Get timestamp
    """
    return datetime.now().timestamp()