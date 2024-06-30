# from typing import List

# from fastapi import APIRouter, Body, HTTPException, status
# from models.users import User

# users_router = APIRouter(
#     tags=["Users"]
# )


# @users_router.get("/", response_model=List[User])
# async def retrieve_all_users() -> List[User]:
#     return users

# @users_router.post("/")
# async def create_user(body: User = Body(...)) -> dict:
#     return {
#         "message": "User created succesfully"
#     }

# @users_router.get("/{id}")
