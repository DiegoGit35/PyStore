# from database.connection import engine
from sqlmodel               import Field, Session, SQLModel, create_engine, select
from typing                 import List
from fastapi                import Depends
from sqlmodel import Session, select
from models.users           import User
from .i_repository          import IRepository

# from services.item_service import ItemService  # Asegúrate de importar correctamente la clase Item
# from entities.item import Item



class UserRepository(IRepository[User]):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.exec(select(User)).all()

    def get_by_id(self, id: int) -> User:
        return self.session.get(User, id)

    def create(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update(self, user: User) -> User:
        # Implementar la lógica para actualizar
        pass

    def delete(self, user: User) -> User:
        # Implementar la lógica para eliminar
        pass