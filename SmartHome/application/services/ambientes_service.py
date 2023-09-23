# EXECUTA AS AÇÕES DA API

from persistence.utils import obter_engine

class AmbienteService():

    def __init__(self) -> None:
        self.session = Session(obter_engine())

    def obter_todos_ambientes():
        session = session(engine)
        intrucao = select(Ambiente)
        ambiente = self.session