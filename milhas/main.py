from fastapi import FastAPI, response
from sqlmodel import SQLModel
app = FastAPI()
class maopdsjfakljs(SQLModel):
    bunda: str

@app.post("/simulacao-compra")
def simular_compra(quantidade:int, desconto:int, bonus:int):
    ref = 70
    valor_desconto = ref - (ref*(desconto/100))
    milhas_bonus = quantidade*(bonus/100)
    valor_a_pagar = valor_desconto * (quantidade/1000)
    milhas_receber = quantidade + milhas_bonus
    valor_real_milheiro = valor_a_pagar/(milhas_receber/1000)
    response = {"Quantidade": quantidade,
                "Desconto": desconto,
                "Bônus": bonus,
                "Valor com Desconto": valor_desconto,
                "Milhas bônus": milhas_bonus,
                "Valor a pagar": valor_a_pagar,
                "Milhas a Receber": milhas_receber,
                "Valor real do milheiro": valor_real_milheiro
                }
    return {"message": response}

