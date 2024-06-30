from sqlmodel import SQLModel, Field

class Categories(SQLModel, table=True):
    id: int =Field(default=None, primary_key = True)
    name: str



    class Config:
        schema_extra={
            "schema":{
                "name": "Electronica"
            }
        }