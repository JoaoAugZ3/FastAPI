from fastapi import status, HTTPException, APIRouter

router = APIRouter()
prefix = '/pessoas'

@router.get('/')
def get_peoples():
    
    return

@router.push('/')
def push_people():
    return

@router.get('/')
def search_people(termo:str):
    return

@router.get('/contagem-pessoas')
def count_people():
    return

