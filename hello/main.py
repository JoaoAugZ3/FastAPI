from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()

proximo_id = 3

class Animal(BaseModel):
    id: int | None = None
    nome: str
    ano_nascimento: int
    cor: str

a1 = Animal(id=1, nome='Rabito', ano_nascimento=2012, cor='Branco')
b1 = Animal(id=2, nome='Bolota', ano_nascimento=2010, cor='Marrom')


animals = [a1, b1]

def buscar_animal_por_id(id:int):
    for animal in animals:
        if animal.id == id:
            return animal
    return None

@app.get('/hello')
def hello():
    return {"mensagem": "Olá, seja bem-vindo."}


@app.get('/animais/{id}')
def obter_um_animal(id:int):
    animal = buscar_animal_por_id(id)
    if not animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Animal não localizado.')
    return animal

@app.get('/animais')
def obter_animais():
    return animals

@app.post('/animais', status_code=status.HTTP_201_CREATED)
def novo_animal(animal: Animal):
    global proximo_id
    animal.id = proximo_id
    proximo_id += 1
    animals.append(animal)
    return None

def remover_animal(id:int):
    animal = buscar_animal_por_id(id)
    if not animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Animal inexistente')
    animals.remove(animal)

@app.get('/donos/{nome}')
def seu_nome(nome:str,):
    return {'mensagem': f'Olá {nome}, seja bem-vindo!'}

@app.get('/meusanimais')
def animais(nome:str, idade:int):
    return {'Mensagem': f'O nome do meu animal é {nome} e ele tem {idade} anos.'}