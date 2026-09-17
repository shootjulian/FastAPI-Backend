from fastapi import FastAPI

app = FastAPI() #Creo un objeto "app" de la clase FastAPI

"""
def root():
    return "Hola, FastAPI" #Simplemente es un codigo python puro y duro
"""
@app.get("/") #Esta rotuer es el de la pagina de inicio, por asi decirlo
async def root(): # Función asíncrona que FastAPI ejecutará cuando llegue una petición GET a "/"
    return "Hola, FastAPI"

@app.get("/url")
async def url():
    return {"url_curso":"https://mourdev.com/python"} #Retorna un JSON
