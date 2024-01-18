from fastapi import APIRouter, Response
from config.db import conn
from models.user_db import users
from schema.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)
user = APIRouter()

@user.get("/users")
def get_users():
    datos_usuarios = conn.execute(users.select()).fetchall()
    columns_names = users.columns.keys()
    lista_de_diccionarios = [dict(zip(columns_names, fila)) for fila in datos_usuarios]
    return lista_de_diccionarios

@user.post("/users")
def create_user(usuario: User):
    new_user = {"name": usuario.name,"email": usuario.email}
    new_user["password"] = f.encrypt(usuario.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    data = conn.execute(users.select().where(users.c.id == result.lastrowid)).first()   
    return data._asdict()

@user.get('/users/{id}')
def get_user(id: str):
    data = conn.execute(users.select().where(users.c.id == id)).first()   
    return data._asdict()

@user.delete('/users/delete/{id}')
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/users/put/{id}')
def update_user(id: str, usuario: User):
    conn.execute(users.update().values(name = usuario.name, email = usuario.email, password = f.encrypt(usuario.password.encode("utf-8"))).where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
