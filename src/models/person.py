from beanie import Document
from pydantic import EmailStr
from pydantic import Field
import uuid

class Person(Document):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")

    first_name: str
    last_name: str
    middle_name: str | None = None

    phone: str | None = None    
    email: EmailStr | None = None
    
    class Settings:
        name = "persons"