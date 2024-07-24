# from database.connection import engine
from typing         import List
from fastapi        import Depends, HTTPException
from sqlmodel       import Field, Session, SQLModel, create_engine, select
from models.users   import User, UserUpdate
from .i_repository  import IRepository

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

    def update(self, id_user: int, user: UserUpdate) -> User:

        db_user = self.session.get(User, id_user)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        user_data = user.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(db_user, key, value)
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def delete(self, user_id: int) -> User:
        user = self.session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.is_active = False
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user