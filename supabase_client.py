from sqlmodel import Session, create_engine
from smarthome.presentation.viewmodels.models import Ambiente
 # Importe seu modelo Ambiente aqui

# Função para adicionar um ambiente ao banco de dados
def adicionar_ambiente():
    # Crie uma engine para se conectar ao banco de dados
    db_url = 'postgresql+psycopg2://postgres:531spxznfknigrd@db.uukrdqjukgqmuqtsxjxy.supabase.co:5432/postgres'
    engine = create_engine(db_url)

    # Crie uma sessão para interagir com o banco de dados
    with Session(engine) as session:
        # Crie uma instância do modelo Ambiente com os dados que você deseja adicionar
        novo_ambiente = Ambiente(nome="Sala de Estar", desc="Descrição da sala de estar", icone="icone.png")

        # Adicione o ambiente à sessão
        session.add(novo_ambiente)

        # Commit (salve) as alterações no banco de dados
        session.commit()

# Função para consultar todos os ambientes no banco de dados
def consultar_ambientes():
    # Crie uma engine para se conectar ao banco de dados
    db_url = 'sua_url_do_banco_de_dados'
    engine = create_engine(db_url)

    # Crie uma sessão para interagir com o banco de dados
    with Session(engine) as session:
        # Crie uma consulta para todos os ambientes
        consulta = session.query(Ambiente)

        # Execute a consulta e obtenha os resultados
        resultados = consulta.all()

        # Imprima os resultados
        for ambiente in resultados:
            print(f"ID: {ambiente.id_amb}, Nome: {ambiente.nome}, Descrição: {ambiente.desc}, Ícone: {ambiente.icone}")

# Chame as funções para adicionar e consultar
adicionar_ambiente()
consultar_ambientes()
