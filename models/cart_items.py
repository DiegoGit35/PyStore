from sqlmodel import SQLModel, Field
from typing import Optional

class CartItems(SQLModel, table = True):
    id:         Optional[int] | None = Field(default = None, primary_key = True, nullable=False)
    cart_id:    int | None = Field(default = None, foreign_key = "cart.id")
    product_id: int | None = Field(default = None, foreign_key = "product.id")
    quantity:   int
    subtotal:   float

    class Config:
        schema_extra: {
            "schema": {
                "cart_id": 3,
                "product_id": 4,
                "quantity": 3,
                "subtotal": 150.00
            }
        }