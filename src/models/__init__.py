from .cabinet import Cabinet
from .user import User, UserAudit
from .person import Person

from beanie import Document

# List of all models in the application
MODELS: list[Document] = [Cabinet, User, UserAudit, Person]