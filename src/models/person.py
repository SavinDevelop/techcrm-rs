from beanie import Document
from pydantic import EmailStr


class Person(Document):
    first_name: str
    last_name: str
    middle_name: str | None = None

    phone: str | None = None    
    email: EmailStr | None = None
    
    class Settings:
        name = "persons"