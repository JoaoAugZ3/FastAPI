from sqlmodel import Session, create_engine, SQLModel, Field

# Defina um modelo para a tabela de teste
class TestTable(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str

# Função para criar a tabela de teste
def create_test_table():
    # Substitua com sua URL de conexão real
#    db_url = 'postgresql+psycopg2://postgres:531spxznfgnikrd@db.uukrdqjukgqmuqtsxjxy.supabase.co:5432/postgres'
    db_url = 'postgresql://postgres:531spxznfgnikrd@db.uukrdqjukgqmuqtsxjxy.supabase.co:5432/postgres'
    engine = create_engine(db_url)

    # Crie a tabela no banco de dados
    SQLModel.metadata.create_all(engine)

    print("Tabela de teste criada com sucesso.")

# Chame a função para criar a tabela de teste
create_test_table()
