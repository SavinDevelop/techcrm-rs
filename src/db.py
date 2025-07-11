from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from .models.user import User
from .models.person import Person 

async def db_init():
    client = AsyncIOMotorClient("mongodb://admin:admin@localhost:27017")

    await init_beanie(
        database=client.techcrm,
        document_models=[User, Person]
        )
