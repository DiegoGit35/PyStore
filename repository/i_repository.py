from typing import List, TypeVar, Generic, Optional
from abc import ABC, abstractmethod
from sqlmodel import SQLModel

T = TypeVar('T', bound=SQLModel)

class IRepository(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, entity: T) -> T:
        pass