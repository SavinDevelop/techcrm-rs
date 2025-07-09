from src.models.user import User

class AuthService:
    async def login(self, email: str, password: str) -> bool:
        user = await User.find_one(User.email == email)
        if user and user.password == password:
            return True
        return False
    
    async def refresh_token(self, user_id: str) -> str:
        return f"new_token_for_user_{user_id}"