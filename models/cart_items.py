from sqlmodel import SQLModel, Field

class CartItems(SQLModel, table = True):
    id:         int | None = Field(default = None, primary_key = True)
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