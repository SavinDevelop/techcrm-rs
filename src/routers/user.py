from fastapi import APIRouter, HTTPException

from src.repositories.user import UserRepository
from src.models.user import User


user_router = APIRouter(prefix="/admin/user", tags=["user"])

@user_router.get("/")
async def get_all_users() -> list[User]:
    return await UserRepository.get_all_users()


@user_router.get("/{user_id}")
async def get_user_by_id(user_id: str):
    user = await UserRepository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user_router.get("/{email}")
async def get_user_by_email(email: str):
    user = await UserRepository.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user_router.post("/")
async def create_user(user: User):
    created_user = await UserRepository.create_user(user)
    return created_user


@user_router.put("/{user_id}")
async def update_user(user_id: str, user: User):
    existing_user = await UserRepository.get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.id = user_id
    updated_user = await UserRepository.update_user(user)
    return updated_user


@user_router.delete("/{user_id}")
async def delete_user(user_id: str):
    existing_user = await UserRepository.get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    
    await UserRepository.delete_user(user_id)
    return {"message": "User deleted successfully"}
