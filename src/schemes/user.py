from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    password: str

    : 
    permission: dict = {"administration": False}
    updated_at: str | None = None
    created_at: str | None = None

    class Config:
        orm_mode = True