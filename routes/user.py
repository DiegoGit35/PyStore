from fastapi import APIRouter, Path, HTTPException, status
from models.users import User 

user_router = APIRouter()

users = []

@user_router.get("/users", status_code=200)
async def get_users() -> dict:
    return{
        "users": "Get all users"
    }


@user_router.post("/users", status_code= 201)
async def add(user: User) -> dict:
    users.append(user)
    return {
        "message": "Create user"
    }


@user_router.get("/users/{user_id}")
async def get_user() -> dict:

    return { 
        "message": f"Get user {user_id}"
        }


@user_router.put("/users/{user_id}", status_code=200)
async def update_user(user_id: int, updated_user: User) -> dict:
    return {
            "message": "User updated successfully"
            }


@user_router.delete("/users/{user_id}")
async def delete_user(user_id: int) -> dict:
      return {
            "message": "User deleted successfully"
            }
