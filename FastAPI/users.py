from fastapi import FastAPI
from pydantic import BaseModel # Definir entidades

app = FastAPI()

# Correr servidor local Uvicorn: fastapi dev users.py

# Entidad User
# BaseModel nos da la capacidad de crear una entidad.
class User(BaseModel):
    id: int
    name: str
    lastname: str
    rol: str
    age: int


# Imaginemos que users es nuestra BD ficticia: users_list
# Instanciamos entidad User, y al ser BaseModel, debemos especificar los parametros:
# Por lo general en una clase normal python podemos mandar los parametros como queramos.
# Pero la clase User esta heredando un comportamiento de BaseModel, por eso debemos especificar.
# Si hacemos peticion a /users, nos retornara un JSON

users_list = [User(id = 1, name = "Sebastian", lastname = "Casadiegos", rol = "Desarrollador backend", age = 25),
              User(id = 2, name = "Andres", lastname = "Casadiegos", rol = "Desarrollador fullstack", age = 27),
              User(id = 3, name = "Santiago", lastname = "Casadiegos", rol = "Estudiante", age = 17)]

"""
# Manual sin instancia. Ejemplo sin Pydantic - BaseModel
@app.get("/usersjson")
async def usersjson():

    # Retornar formato JSON
    return [
        {
            "name": "Sebastian",
            "lastname": "Casadiegos",
            "rol": "Desarrollador backend",
            "age": 25
        },
        {
            "name": "Andres",
            "lastname": "Casadiegos",
            "rol": "Desarrollador fullstack",
            "age": 27
        },
        {
            "name": "Kevin",
            "lastname": "Casadiegos",
            "rol": "Estudiante",
            "age": 17
        },
    ]
"""

# Get de usuarios
@app.get("/users")
async def users():
    return users_list


# Path = pasar informacion a nuestra API.
@app.get("/user/{id}")
async def user(id: int): # FastAPI trabaja tipando el tipo de dato.
    return search_user(id)
    

# Query: /?campo=valor
@app.get("/user/")
async def userquery(id: int): # FastAPI trabaja tipando el tipo de dato.
    return search_user(id)

    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list) # Objeto filter
    
    try:
        # Convertimos a lista y devolvermos el primero.
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario."}