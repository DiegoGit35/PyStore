# from database.connection import engine
from sqlmodel               import Field, Session, SQLModel, create_engine, select
from typing                 import List
from fastapi                import Depends
from .i_repository          import IRepository
from models.users           import User
from database.connection    import get_session
# from services.item_service import ItemService  # Asegúrate de importar correctamente la clase Item
# from entities.item import Item



class UserRepository(IRepository):
    # def __init__(self):
    #     self.entities = []

    async def get_all(self, session=Depends(get_session)):
        # statement = select(User)
        # results = await session.exec(statement)
        # for user in results:
        #     print(user)
        # return results
        return {
            "message": "getted"
        }

    def get_by_id(self, id) -> User:

        pass

    def create(self, user: User) -> User:
        session = Session(engine)
        session.add(user)
        session.commit()
        session.close

    def update(self, user: User) -> User:
        # Implementar la lógica para actualizar
        pass

    def delete(self, user: User) -> User:
        # Implementar la lógica para eliminar
        pass