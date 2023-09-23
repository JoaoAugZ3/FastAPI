from fastapi import FastAPI
from sqlmodel import SQLModel
app = FastAPI()

@app.post("/simulacao-compra")
def simular_compra(quantidade: int, desconto:int, bonus: int):
    pass