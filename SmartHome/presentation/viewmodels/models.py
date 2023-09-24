from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship


class Dispositivo(SQLModel, table=True):
    id_dispo: int = Field(primary_key=True, index=True)
    desc: str
    icone: str
    status_conexao: bool
    status_lig_desl: bool
    ambiente_id: int = Field(foreign_key="ambiente.id_amb")

class Ambiente(SQLModel, table=True):
    id_amb: int = Field(primary_key=True, index=True)
    nome: str
    desc: str
    icone: str


    # Defina a relação com os dispositivos
    dispositivos: list[Dispositivo] = Relationship(back_populates="ambiente")