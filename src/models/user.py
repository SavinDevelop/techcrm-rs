from typing import Annotated
from beanie import Document, Indexed, Link
from pydantic import EmailStr, BaseModel

from .person import Person


class Permission(BaseModel):
    administartion: bool = False


class User(Document):
    email: Annotated[EmailStr, Indexed(unique=True)]
    password: str

    profile: Link[Person] | None = None
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
