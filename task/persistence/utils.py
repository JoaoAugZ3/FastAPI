from sqlmodel import create_engine, SQLModel
#PUXA OS DADOS DO .ENV
from decouple import config

def get_engine():
    HOST = config('DB_HOST')
    PORT = config('DB_PORT')
    USER = config('DB_USER')
    DATABASE = config('DB_DATABASE')
    PASSWORD = config('DB_PASSWORD')
    
    db_url = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    engine = create_engine(db_url, echo=True)
    
    return engine

def create_all_tables():
    engine = create_engine()
    SQLModel.metadata.create_all(engine)