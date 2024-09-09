from fastapi import FastAPI
from user import User
from bd import Bd
from pydantic import BaseModel

app = FastAPI()

bd = Bd()

user1 = User("João", 123456789, "01/01/2000")
user2 = User("Maria", 987654321, "02/02/2000")
user3 = User("José", 123123123, "03/03/2000")

bd.addUser(user1)
bd.addUser(user2)
bd.addUser(user3)

class UserSave(BaseModel):
    name: str
    cpf: int
    data_nascimento: str

@app.get("/")
async def root():
    return {"message": "Tudo Funcionando"}

@app.get("/getUsers/{cpf}")
async def root(cpf: int):
    user = bd.getUser(cpf)

    if user == None:
        response = {"message": "CPF não cadastrado"}
    else:
        response = {"name": user.getName(), "cpf": user.getCpf(), "data_nascimento": user.getDataNascimento()}

    return response

@app.post("/addUser")
async def root(user: UserSave):
    newUser = User(user.name, user.cpf, user.data_nascimento)
    
    if (bd.getUser(newUser.getCpf()) == None):
        response = {"name": newUser.getName(), "cpf": newUser.getCpf(), "data_nascimento": newUser.getDataNascimento()}
        bd.addUser(newUser)
    else :
        response = {"message": "CPF já cadastrado"}

    # bd.showUsers()

    return response

@app.get("/showUsers")
async def root():
    bd.getUsers()

    response = {}
    i=0
    for user in bd.getUsers():
        userAux = {"name": user.getName(), "cpf": user.getCpf(), "data_nascimento": user.getDataNascimento()}
        response.update({i: userAux})
        i+=1
        
    return response

