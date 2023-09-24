import uuid
from typing import List
from sqlmodel import Session, create_engine, SQLModel, Field

# Defina um modelo para a tabela de ambiente
class Ambiente(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    descricao: str
    icone: str
    dispositivos: List[str]

# Função para criar a tabela de ambiente
def create_ambiente_table():
    # Substitua com sua URL de conexão real
    db_url = 'postgresql://postgres:531spxznfgnikrd@db.uukrdqjukgqmuqtsxjxy.supabase.co:5432/postgres'
    engine = create_engine(db_url)

    # Crie a tabela no banco de dados
    SQLModel.metadata.create_all(engine)

    print("Tabela de ambiente criada com sucesso.")

# Chame a função para criar a tabela de ambiente
create_ambiente_table()
