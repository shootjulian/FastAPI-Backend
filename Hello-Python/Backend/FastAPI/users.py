from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url : str
    age: int


users_list = [User(id=1, name="Juan", surname="Salamanca", url="https://moure.dev", age=35),
            User(id=2, name="Angel", surname="Manuel", url="https://mourdev.com", age=20),
            User(id=3, name="Alejandro", surname="Perez", url="https://moure.co", age=45)]


# python -m uvicorn users:app --reload
@app.get("/usersjson")
async def usersjson():
    return [{"name": "Julian"},
            {"name": "Pepe el grillo"}]

@app.get("/userclass")
async def userclass():
    return User(name="Julian", surname="Mendez", url="https://moure.dev", age= 35)


@app.get("/users/")
async def users():
    return users_list

#Path
@app.get("/users/{id}")
async def users(id: int):
    users = filter(lambda user: user.id == id, users_list)

    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

#Query
@app.get("/user")
async def users(id: int):
    return serach_user(id)

@app.post("/createuser") #Mejor singular, para indicar que se va a crear un solo user
async def user(user: User):
    users_list.append(user)

    return {
        "message": "Usuario creado exitosamente, gracias por tu JSON que pasamos a objeto User",
        "user": user
    }


def serach_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
            return {"error": "No se ha encontrado el usuario"}


