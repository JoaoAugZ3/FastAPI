# CONTROLE DAS ROTAS DE AMBIENTES

from fastapi import status, HTTPException, APIRouter
from presentation.viewmodels.models import *
#from sqlmodel import Session, delete, select

#MUDAR AS FUNÇÕES PARA UM ARQUIVO SEPARADO DEPOIS   
#def buscar_ambiente(id_amb: int):
#    for ambiente in residencia   :
#        if ambiente.id_amb == id_amb:
#            return ambiente
#        else:
#            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente inexistente.')


router = APIRouter()
prefix = '/ambientes'
ambientes_services = ambientes_services
#app = APIRouter()
#router.get()

@app.get('/')
async def mostrar_ambientes():
    return residencia

@app.get('/{id_amb}')
def buscar_um_ambiente(id_amb:int):
    ambiente = buscar_ambiente(id_amb)
    if ambiente == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente inexistente.')
    return ambiente

@app.post('/')
def post_ambiente(ambiente: Ambiente):
    global next_id
    ambiente.id_amb = next_id
    next_id += 1
    residencia.append(ambiente)
    return ambiente

# Para atualizar o ambiente o antigo terá que ser removido da residência e depois adicionado o atualizado.
@app.put('/')
def put_ambiente(ambiente: Ambiente):
    residencia.remove(ambiente)
    residencia.append(ambiente)
    return residencia

@app.delete('/{id_amb}')
def delete_ambiente(id_amb:int):    
    ambiente = buscar_ambiente(id_amb)
    if not ambiente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente inexistente.')
    if len(ambiente.dispositivos) == 0:
        residencia.remove(ambiente)