# CONTROLE DAS ROTAS DE environmentS
from fastapi import status, HTTPException, APIRouter

from presentation.viewmodels.models import *
from ...persistence.utils import get_engine
from ...application.services.environments_service import EnvironmentService

engine = get_engine()
router = APIRouter()
prefix = '/environments'

environment_service = EnvironmentService()


@router.get('/', status_code=status.HTTP_200_OK)
async def show_environments():
    return environment_service.get_all_environment

@router.get('/{id}', status_code=status.HTTP_200_OK)
def search_an_environment(id:str):
    environment = environment_service.get_environment_for_id(id)

    if not environment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Environment not found')
    
    return environment
    
@router.post('/')
def post_environment(environment: Environment):
    return environment_service.create_environment(environment)


@router.put('/')
def put_environment(id:str,environment: Environment):
    return environment_service.update_environment(id, environment)

@router.delete('/{id}')
def delete_environment(id:str):    
    environment = search_an_environment(id)
    if not environment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Environment not found')
    environment_service.delete_environment(id)