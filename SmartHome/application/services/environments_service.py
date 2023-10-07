#FEITO AS FUNÇÕES DO AMBIENTE

# EXECUTA AS AÇÕES DA API
from fastapi import HTTPException, status
from sqlmodel import Session, delete, select
from persistence.utils import get_engine
from presentation.viewmodels.models import *


class EnvironmentService:
    def __init__(self) -> None:
        self.session = Session(get_engine())


    def get_all_environment(self):
        sttm = select(Environment)
        environments = self.session.exec(sttm).fetchall()
        self.session.close()
        
        return environments
    

    def get_environment_for_id(self, id:int):
        sttm = select(Environment).where(Environment.id == id)
        environment = self.session.exec(sttm).first()
        self.session.close()
        
        return environment
    

    def create_environment(self, environment:Environment):
        self.session.add(Environment)
        self.session.commit()
        self.session.refresh(environment)
        

    def update_environment(self, id:str, environment:Environment):
        current_environment = self.get_environment_for_id(id)
        
        if not current_environment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Environment not found')
        
        current_environment.description = environment.description
        
        self.session.add(current_environment)
        self.session.commit()
        self.session.close()
        
        
    def delete_environment(self, id:str):
        environment = self.get_environment_for_id(id)
        
        if not environment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Environment not found')
        
        environment_devices = select(Environment).where(Environment.id == id and Environment.devices > 0)

        sttm = delete(Environment).where(Environment.id == id)
        self.session.exec(sttm)
        self.session.commit()
        self.session.close()