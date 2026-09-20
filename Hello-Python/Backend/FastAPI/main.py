# Importamos la clase FastAPI desde el paquete/librería fastapi.
#
# En Java sería conceptualmente parecido a:
# import fastapi.FastAPI;
#
# "fastapi" = paquete/librería
# "FastAPI" = clase que queremos usar
from fastapi import FastAPI


# Creamos un objeto llamado "app" a partir de la clase FastAPI.
#
# En Java sería parecido a:
# FastAPI app = new FastAPI();
#
# En Python no escribimos el tipo ni usamos "new":
# app = FastAPI()
#
# FastAPI  -> clase
# FastAPI() -> constructor / creación del objeto
# app       -> variable que referencia ese objeto
app = FastAPI()


# Servidor local:
# http://127.0.0.1:8000
#
# 127.0.0.1 significa "mi propio computador"
# 8000 es el puerto donde Uvicorn está escuchando.


# Este decorador registra una ruta dentro del objeto "app".
#
# Le estamos diciendo a FastAPI:
# "Cuando llegue una petición HTTP GET al path '/', ejecuta
# la función que aparece inmediatamente debajo."
#
# GET = operación HTTP
# "/" = path
#
# Juntos forman este endpoint:
# GET /
@app.get("/")
async def root():

    # Esta es la respuesta que FastAPI devolverá al cliente.
    #
    # Por ejemplo:
    # navegador -> GET /
    # FastAPI   -> ejecuta root()
    # root()    -> devuelve "Hola FastAPI!"
    return "Hola FastAPI!"


# Otra URL disponible:
# http://127.0.0.1:8000/url


# Registramos otro endpoint:
#
# GET /url
#
# Es importante notar que:
#
# GET /       -> un endpoint
# GET /url    -> otro endpoint
#
# Aunque ambos pertenecen a la misma aplicación "app".
@app.get("/url")
async def url():

    # Aquí no devolvemos solamente un String.
    # Devolvemos un diccionario de Python.
    #
    # Python:
    # {"url": "https://mouredev.com/python"}
    #
    # Conceptualmente se parece a enviar un objeto con:
    #
    # clave  -> "url"
    # valor  -> "https://mouredev.com/python"
    #
    # FastAPI convierte automáticamente este diccionario
    # a JSON para enviarlo al cliente.
    return {"url": "https://mouredev.com/python"}


# ---------------------------------------------------------
# EJECUCIÓN DEL SERVIDOR
# ---------------------------------------------------------

# En el curso:
# uvicorn main:app --reload
#
# En mi computador:
# python -m uvicorn main:app --reload
#
# main -> archivo main.py
# app  -> objeto creado arriba con app = FastAPI()
#
# Es decir:
# "Uvicorn, abre main.py y ejecuta la aplicación llamada app."


# --reload:
# Uvicorn vigila cambios en los archivos del proyecto.
# Si modificamos el código y guardamos, reinicia automáticamente
# el servidor para cargar los cambios.


# Detener el servidor:
# CTRL + C


# ---------------------------------------------------------
# DOCUMENTACIÓN AUTOMÁTICA
# ---------------------------------------------------------

# Swagger UI:
# http://127.0.0.1:8000/docs
#
# Permite ver y probar nuestros endpoints desde una página web.


# ReDoc:
# http://127.0.0.1:8000/redoc
#
# Otra interfaz para visualizar la documentación de nuestra API.