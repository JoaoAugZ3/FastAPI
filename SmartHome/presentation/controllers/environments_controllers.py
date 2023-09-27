# CONTROLE DAS ROTAS DE AMBIENTES
from fastapi import status, HTTPException, APIRouter

from presentation.viewmodels.models import *
from ...persistence.utils import get_engine
from ...application.services.environments_service import EnvironmentService

engine = get_engine()
router = APIRouter()
prefix = '/environments'

environment_service = EnvironmentService()
#router = APIRouter()
#router.get()

@router.get('/', status_code=status.HTTP_200_OK)
async def mostrar_ambientes():
    return environment_service.get_all_environment

@router.get('/{id}', status_code=status.HTTP_200_OK)
def buscar_um_ambiente(id:str):
    environment = environment_service.get_environment_for_id(id)

    if not environment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Environment not found')
    
    return environment
    
@router.post('/')
def post_ambiente(environment: Environment):
    return environment_service.create_environment(environment)


@router.put('/')
def put_ambiente(id:str,environment: Environment):
    return environment_service.update_environment(id, environment)

@router.delete('/{id_amb}')
def delete_ambiente(id_amb:int):    
    ambiente = buscar_ambiente(id_amb)
    if not ambiente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente inexistente.')
    if len(ambiente.dispositivos) == 0:
        residencia.remove(ambiente)