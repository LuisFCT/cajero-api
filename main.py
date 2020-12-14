from db.user_db import UserInDB                  #Traemos la informacion del usuario en la base de datos
from db.user_db import update_user, get_user

from db.transaction_db import TransactionInDB    #Traemos la información en la transacción
from db.transaction_db import save_transaction

from models.user_models import UserIn, UserOut   #Traemos los modelos de usuario(estados)

from models.transaction_models import TransactionIn, TransactionOut #Traemos los modelos de transacción(estadoos)

import datetime                         #Se Importan algunos paquetes adicionales
from fastapi import FastAPI             #Para crear la API
from fastapi import HTTPException       #Se utiliza para lanzar errores, excepciones

api = FastAPI()     #Creamos la API-REST(aplicación)

#Comunicación entre capa logica y de presentación

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "https://cajero-app164.herokuapp.com"
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

mensaje : str = "El usuario no existe"

#Implementamos las operaciones
#1 Operación autenticar usuario (auth_user)
@api.post("/user/auth/")   #Decorador para asociar una función a un servicio web(@api."aqui_el_servicio"("aqui_la_URL"))
async def auth_user(user_in: UserIn):          #async: cuando llega la peticion la pone a correr (muchos procesos a la vez)
    user_in_db = get_user(user_in.username)    #LLama a la funcion get_user para buscar un usuario
    if user_in_db == None:                     #Si el usuario no esta en la BD lanza un error
        raise HTTPException(status_code=404, detail=mensaje)  #raice para lanzar la exception
    if user_in_db.password != user_in.password:   #Si el usuario esta en la base y la contraseña coincide con la base de datos retorna autenticado
        return {"Autenticado": False}
    return {"Autenticado": True}

#2 Operación Consultar saldo (get_balance)
@api.get("/user/balance/{username}")
async def get_balance(username : str):
    user_in_db = get_user(username)      #Se verifica si el usuario esta en la base de datos
    if user_in_db == None:               #Si el usuario no esta se lanza un error
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())   #Mapea lo que viene e user_in_db y lo vuelve en un diccionario
    return user_out                           #Retorna esa salida

#3 Operación retirar dinero (make_transaction)
@api.put("/user/transaction/")
async def make_transaction(transaction_in : TransactionIn):
    user_in_db = get_user(transaction_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail=mensaje)
    if user_in_db.balance < transaction_in.value:
        raise HTTPException(status_code=400, detail="Sin fondos suficientes")
    user_in_db.balance = user_in_db.balance - transaction_in.value
    update_user(user_in_db)
    transaction_in_db = TransactionInDB(**transaction_in.dict(), actual_balance = user_in_db.balance)
    transaction_in_db = save_transaction(transaction_in_db)
    transaction_out = TransactionOut(**transaction_in_db.dict())
    return transaction_out

