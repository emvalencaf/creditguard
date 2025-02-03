from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import etl_settings
from helpers.logging import etl_logging
DBBaseModel = declarative_base()

DATABASE_URL = etl_settings.DB_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

def get_db():
    """
    Provides a database session to be used within a request context.
    
    :return: A SQLAlchemy database session instance.
    """
    etl_logging.info("Creating a session with database...")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()