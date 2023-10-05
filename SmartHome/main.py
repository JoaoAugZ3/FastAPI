from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from presentation.viewmodels.models import *
from presentation.controllers.ambiente_controllers import \
    router as ambientes_router, prefix as ambientes_prefix
from presentation.controllers.dispositivos_controllers import\
    router as dispositivos_router

app = FastAPI()
create_tables() 
#app.include_router(ambientes_router, prefix=ambiente_prefix)
#app.include_router(dispositivos_router, prefix='/dispositivos')

#implementar banco de dados assim que possível
residencia = []
next_id = 1