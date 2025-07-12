from src.models.user import User

class UserRepository:
    @staticmethod
    async def create_user(user: User) -> User:
        await user.insert()
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> User | None:
        return await User.find_one(User.email == email)
    
    @staticmethod
    async def get_user_by_id(user_id: str) -> User | None:
        return await User.get(user_id)
    
    @staticmethod
    async def get_all_users() -> list[User]:
        return await User.find_all().to_list()

    @staticmethod
    async def update_user(user: User) -> User:
        await user.save()
        return user

    @staticmethod
    async def delete_user(user_id: str) -> None:
        user = await User.get(user_id)
        if user:
            await user.delete()