from os import makedirs

def ensure_dir(directory: str):
    """
    Ensures that directory exists, if not exist it will create.
    
    :param directory: directory path
    """
    makedirs(directory,
             exist_ok=True)