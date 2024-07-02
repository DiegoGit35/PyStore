from typing import List, TypeVar
from abc import ABC, abstractclassmethod

T = TypeVar('T')

class IRepository(ABC):
    @abstractclassmethod
    def get_all(self) -> List[T]:
        pass

    @abstractclassmethod
    def get_by_id(self, id: int) -> T:
        pass

    @abstractclassmethod
    def create(self, entity: T) -> T:
        pass

    @abstractclassmethod
    def update(self, entity: T) -> T:
        pass

    @abstractclassmethod
    def delete(self, entity: T) -> T:
        pass