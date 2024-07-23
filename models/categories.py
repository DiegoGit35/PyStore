from sqlmodel import SQLModel, Field
from typing import Optional

class Categories(SQLModel, table=True):
    id:     Optional[int] = Field(default=None, primary_key = True, nullable=False)
    name:   str



    class Config:
        schema_extra={
            "schema":{
                "name": "Electronica"
            }
        }