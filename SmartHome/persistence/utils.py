from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os
load_dotenv()

def get_engine():
    HOST = os.getenv('DB_HOST')
    USER = os.getenv('DB_USER')
    DATABASE = os.getenv('DB_DATABASE')
    PORT = os.getenv('DB_PORT')
    PASSWORD = os.getenv('DB_PASSWORD')
    
    db_url = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    engine = create_engine(db_url, echo=True)
    return engine


def create_table():
    SQLModel.metadata.create_all(get_engine())