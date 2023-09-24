from sqlmodel import create_engine, select, delete, update, Session
from ..presentation.viewmodels.models import Ambiente


def obter_engine():
    db_url = 'postgresql+psycopg2://postgres:531spxznfknigrd@db.uukrdqjukgqmuqtsxjxy.supabase.co:5432/postgres'
    engine = create_engine(db_url, echo=True)

    return engine


engine = obter_engine()
session = Session(engine)


consulta = select(Ambiente)

resultado = session.exec(consulta).all()

print(ambientes.nome)