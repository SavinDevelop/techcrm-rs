from fastapi import FastAPI
from contextlib import asynccontextmanager

from .models.user import User, Person
from .db import db_init
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_init()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/users")
async def get_all_users() -> list[User]:
    return await User.find_all().to_list()

@app.post("/users")
async def create_user(user: User):
    await user.insert()
    return user

@app.get("/persons")
async def get_all_persons() -> list[Person]:
    return await Person.find_all().to_list()

@app.post("/persons")
async def create_person(person: Person):
    await person.insert()
    return person