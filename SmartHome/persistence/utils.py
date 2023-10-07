from sqlmodel import SQLModel, create_engine
#from decouple import config

def get_engine():
    # HOST = config('DB_HOST')
    # USER = config('DB_USER')
    # DATABASE = config('DB_DATABASE')
    # PORT = config('DB_PORT')
    # PASSWORD = config('DB_PASSWORD')
    
    # db_url = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    db_url = 'postgresql+psycopg2://postgres:JoaoAugustoELinfo@db.uukrdqjukgqmuqtsxjxy.supabase.co:5432/postgres'
    engine = create_engine(db_url, echo=True)
    return engine


def create_table():
    SQLModel.metadata.create_all(get_engine())