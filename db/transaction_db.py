from datetime import datetime   #Se importan las librerias
from pydantic import BaseModel

class TransactionInDB(BaseModel):  #Se crea la clase TransactionInDB que hereda o extiende de BaseModel
    id_transaction: int = 0        #Se define el atributo id_transaction como tipo int y su valor por defecto
    username: str
    date: datetime = datetime.now()  ##Se define el atributo date como tipo datetime(fecha y hora)
    value: int
    actual_balance: int

database_transactions = []  #Se define una lista vacia para las transacciones
generator = {"id":0}

def save_transaction(transaction_in_db: TransactionInDB):    #Funcion para guardar las transacciones
    generator["id"] = generator["id"] + 1
    transaction_in_db.id_transaction = generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db