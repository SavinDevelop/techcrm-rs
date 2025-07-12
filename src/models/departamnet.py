from beanie import Document
from pydantic import Field
import uuid

class Departament(Document):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    name: str
    
    class Settings:
        name = "cabinets"