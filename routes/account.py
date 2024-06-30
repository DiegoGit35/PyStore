from fastapi import APIRouter, HTTPException, status
from models.users import User

account_router = APIRouter()


@account_router.get("/me", status_code=200)
async def get_my_info() -> dict:
    return {
        "user": authenticated_user
    }


@account_router.put("/me", status_code=200)
async def edit_my_info(updated_user: User) -> dict:
    return {
        "message": "User info updated successfully"
    }


@account_router.delete("/me")
async def remove_my_account() -> dict:
    return {
        "message": "User account removed successfully"
    }
