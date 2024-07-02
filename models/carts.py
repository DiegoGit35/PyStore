from sqlmodel import SQLModel, Field

class Cart(SQLModel, table= True):
    id:             int | None = Field(default=None, primary_key = True)
    user_id:        int | None = Field(default = None, foreign_key = "user.id")
    created_at:     str
    total_amount:   float

    class Config:
        schema_extra={
            "schema":{
                "user_id": 5,
                "created_at": "2020-08-01-12-39",
                "total_amount": 1020.00
            }
        }