# Paso 0: Instalar -> pip install "fastapi[standard]"

# Paso 1: importa FastAPI
from fastapi import FastAPI

# Paso 2: crea una "instance" de FastAPI
app = FastAPI()

""" 
    1. Accedemos al contexto de FastAPI con @app
    2. Las peticiones a un servidor son asincronas -> async:
        Asincrono: permite atender varias solicitudes al mismo tiempo sin esperar
        que una termine para iniciar otra (no bloquea el servidor).
"""

# Paso 3: crea una path operation decorator
# Url local: http:// 127.0.0.1:8000/
@app.get("/")
async def root(): # Paso 4: define la path operation function
    # Paso 5: retorna el contenido
    return "¡Hola FastAPI!"

# Url local: http:// 127.0.0.1:8000/url
@app.get("/url")
async def url():
    return {
        "url_curso": "https://mouredev.com/python"
    }

# Correr servidor local Uvicorn: fastapi dev main.py

# Documentacion con Swagger: http:// 127.0.0.1:8000/docs
# Documentacion con Redocly: http:// 127.0.0.1:8000/redoc

"""
    Notas:

    1. Debemos tener una sola operación GET a la raíz ("/").
"""