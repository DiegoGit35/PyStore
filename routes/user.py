from fastapi import APIRouter, Path, HTTPException, status, Depends
from sqlmodel import Session
from models.users import User 
from repository.i_repository import IRepository
from repository.user_repository import UserRepository
from database.connection    import get_session


user_router = APIRouter()

# user_repo = UserRepository()

def get_user_repository(session: Session = Depends(get_session)) -> IRepository[User]:
    return UserRepository(session)

# users_list = []

@user_router.get("/users")
def get_users(repo: IRepository[User] = Depends(get_user_repository)):
    return repo.get_all()


@user_router.post("/users")
def add(user: User, repo: IRepository[User] = Depends(get_user_repository)):
    return repo.create(user)


@user_router.get("/users/{user_id}")
def get_user(user_id: int, repo: IRepository[User] = Depends(get_user_repository)) -> dict:
    return  repo.get_by_id(user_id)


@user_router.put("/users/{user_id}", status_code=200)
def update_user(user_id: int, updated_user: User) -> dict:
    return {
            "message": "User updated successfully"
            }


@user_router.delete("/users/{user_id}")
def delete_user(user_id: int) -> dict:
      return {
            "message": "User deleted successfully"
            }
