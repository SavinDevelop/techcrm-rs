from beanie import Document
import uuid
from pydantic import Field

class Cabinet(Document):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    name: str
    
    class Settings:
        name = "cabinets"