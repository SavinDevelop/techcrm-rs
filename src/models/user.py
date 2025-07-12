from typing import Annotated
from beanie import Document, Indexed, Link
from pydantic import EmailStr, BaseModel, Field
import uuid

from .person import Person


class Permission(BaseModel):
    administartion: bool = False

class Settings(BaseModel):
    avatar: str | None = None
    theme: str = "light"

class User(Document):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")

    email: Annotated[EmailStr, Indexed(unique=True)]
    password: str

    person: Link[Person] | None = None
    permission: Permission = Permission()

    updated_at: str | None = None
    created_at: str | None = None

    class Settings:
        name = "users"

class UserAudit(Document):
    user: Link[User]
    action: str     
    timestamp: str  

    class Settings:
        name = "users_audit"