#FEITO
from sqlmodel import create_engine, SQLModel

def get_engine():
    db_url = 'postgresql+psycopg2://postgres:531spxznfknigrd@db.uukrdqjukgqmuqtsxjxy.supabase.co:5432/postgres'
    engine = create_engine(db_url, echo=True)

    return engine

def create_tables():
    SQLModel.metadata.create_all(get_engine)