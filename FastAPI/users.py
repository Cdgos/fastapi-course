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

# GET - Obtener todos los usuarios
@app.get("/users")
async def get_users():
    return users_list


# GET - Path = Obtener un usuario por ID (Path Parameter) - OBLIGATORIOS.
@app.get("/users/{id}")
async def get_user_by_id(id: int): # FastAPI trabaja tipando el tipo de dato.
    return search_user(id)
    

# GET - Query: /?campo=valor (Parametros DINAMICOS: Podemos tener mas de 1. No son obligatorios).
# Mas parametros: /?campo1=valor1&campo2=valor2
@app.get("/users")
async def get_user_by_query(id: int): # FastAPI trabaja tipando el tipo de dato.
    return search_user(id)


# POST: Crear un nuevo usuario
@app.post("/users")
async def create_user(user: User):

    # Vereficamos que no exista
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe."}

    users_list.append(user)
    return user


# PUT: Actualizar un usuario
@app.put("/users")
async def update_user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha encontrado el usuario."}

    return user


# DELETE: Eliminar usuario
@app.delete('/users/{id}')
async def delete_user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha encontrado el usuario."}    


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list) # Objeto filter
    
    try:
        # Convertimos a lista y devolvermos el primero.
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario."}