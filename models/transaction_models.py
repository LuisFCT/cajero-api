from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):   #Se definie el estado TransactionIN de la entidad transacción con sus atributos
    username: str
    value: int

class TransactionOut(BaseModel): #Se definie el estado TransactionOUT de la entidad transacción con sus atributos
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_balance: int

