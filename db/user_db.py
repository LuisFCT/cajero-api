from typing import Dict       #Se importan Dict y BaseModel
from pydantic import BaseModel

class UserInDB(BaseModel):    #Se define la clase UserInDB --> UserInDB(BaseModel): UserInDB hereda de BaseModel --> herencia en python
    username: str             #Se definen el atributo username como tipo str(string)
    password: str             #Se definen el atributo password como tipo str(string)
    balance: int              #Se definen el atributo balance como tipo int(entero)

database_users = Dict[str, UserInDB]    #Creamos una base de datos ficticia --> un diccionario que tiene un str y un UserInDB (clave - valor)
    
#Se empieza a llenar el diccionario o base de datos ficticia
database_users = {                       
    "camilo24": UserInDB(**{"username":"camilo24",   #Los ** estan haciendo un mapeo a los atributos de la clase
                            "password":"root",       #Proceso parecido al instanciamineto de un objeto
                            "balance":12000}),

    "andres18": UserInDB(**{"username":"andres18",   
                            "password":"hola",
                            "balance":34000}),
}

def get_user(username: str):     #Se define una funcion que tiene como entrada un username de tipo str
    if username in database_users.keys(): #Si el usuario esta en las llaves del diccionario retorna el valor de ese username
        return database_users[username]
    else:                    #Si no lo encuentra no retorna nada
        return None

def update_user(user_in_db: UserInDB):  #Se define una funcion que tiene como entrada un user_in_db de tipo UserInDB
    database_users[user_in_db.username] = user_in_db  #Lo busca en el diccionario, si existe lo modifica y si no lo crea
    return user_in_db

