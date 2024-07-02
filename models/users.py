from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id:         int = Field(default=None, primary_key=True)
    username:   str
    email:      str
    password:   str
    full_name:  str
    is_active:  bool
    created_at: str
    role:       str

    class Config:
        schema_extra = {
            "schema":{
                'username' : "janedoe_123",
                'email' : "jane.doe@example.com",
                'password' : "mysecurepassword",
                'full_name' : "Jane Doe",
                'is_active' : True,
                'created_at' : "2023-07-20",
                'role' : "admin"
            }
        }