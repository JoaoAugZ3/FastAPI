from pydantic import BaseModel

class Dispositivo(BaseModel):
    id_dispo: int | None = None
    desc: str
    icone: str
    status_conexao: bool
    status_lig_desl: bool

class Ambiente(BaseModel):
    id_amb: int | None = None
    nome: str
    desc: str
    icone: str
    dispositivos: list[Dispositivo] = []
