from pydantic import BaseModel  #Se importa el BaseModel

class UserIn(BaseModel):    #Se crea el estado UserIn de la entidad Usuario con sus atributos correspondientes
    username: str
    password: str

class UserOut(BaseModel):   #Se crea el estado UserOut de la entidad Usuario con sus atributos corresondientes
    username: str
    balance: int

