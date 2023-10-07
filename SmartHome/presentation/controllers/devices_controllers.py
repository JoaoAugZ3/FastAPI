# from fastapi import APIRouter, status, HTTPException
# from presentation.viewmodels.models import  *
# from application.services.environments_service import *
# #from sqlmodel import Session, delete, select

# router = APIRouter()
# prefix = '/environments/{id}/devices'
 
# engine = get_engine()
# environment_service = EnvironmentService()

# #MUDAR AS FUNÇÕES PARA UM ARQUIVO SEPARADO DEPOIS   
# '''def buscar_dispositivo(origem:Ambiente, id_dispo:int):
#     for dispo in origem.dispositivos:print(ambientes.nome)
#         if dispo.id == id_dispo:
#             return dispo
#         else:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Dispositivo inexistente.')
# '''
# '''def mover_dispositivo(origem:Ambiente, destino:Ambiente, dispositivo:Dispositivo):
#     origem.dispositivos.remove(dispositivo)
#     destino.dispositivo.appende(dispositivo)
#     return destino.dispositivos
# '''

# @router.get('/')
# def show_devices(id_amb:int):
#     ambiente = buscar_ambiente(id_amb)
#     if not ambiente:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente inexistente.')
#     return ambiente.dispositivos

# @router.get('/{id_dispo}')
# def mostrar_um_dispositivo(id_amb:int, id_dispo:int):
#     ambiente = buscar_ambiente(id_amb)
#     dispositivo = buscar_dispositivo(ambiente, id_dispo)
#     if not ambiente and not dispositivo:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente ou dispositivo inexistente.')
    
#     return dispositivo

# @router.post('/')
# def criar_dispostivos(id_amb:int, dispositivo:Dispositivo):
#     ambiente = buscar_ambiente(id_amb)
#     ambiente.dispositivos.append(dispositivo)
#     return ambiente.dispositivos

# @router.put('/{id_dispo}/mover/{id_destino}')
# def mover_um_dispositivo(id_origem:str, id_dispositivo:int, id_destino:str):
#     origem = buscar_ambiente(id_origem)
#     destino = buscar_ambiente(id_destino)
#     dispositivo = buscar_dispositivo(origem, id_dispositivo)

#     mover_dispositivo(origem, destino, dispositivo)

# """
# @router.put('//{id_dispo}')
# def atualizar_dispositivos(id_amb:int, dispositivo:Dispositivo):
#     pass
# """


# @router.delete('/{id_dispo}')
# def delete_dispositivos(id_amb:int, id_dispo:int):
#     ambiente = buscar_ambiente(id_amb)
#     dispositivo = buscar_dispositivo(id_dispo)
#     if not ambiente and not dispositivo:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente ou dispositivo inexistente.')    
    
#     ambiente.dispositivos.remove(dispositivo)    