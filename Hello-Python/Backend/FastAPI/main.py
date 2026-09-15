from fastapi import FastAPI

app = FastAPI() #Creo un objeto "app" de la clase FastAPI

"""
def root():
    return "Hola, FastAPI" #Simplemente es un codigo python puro y duro
"""
@app.get("/")
async def root(): #Siempre que llamamos un servidor, la operacion debe ser asincrona
    return "Hola, FastAPI"
