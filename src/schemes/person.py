from pydantic import BaseModel, EmailStr


class Person(BaseModel):
    id: str
    first_name: str
    last_name: str
    middle_name: str | None = None

    phone: str | None = None    
    email: EmailStr | None = None