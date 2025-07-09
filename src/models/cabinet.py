from beanie import Document


class Cabinet(Document):
    name: str
    
    class Settings:
        name = "cabinets"