from fastapi import FastAPI




app = FastAPI()
@app.post('/singup')
def create_user():
    pass