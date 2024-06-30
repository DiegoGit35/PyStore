from fastapi import APIRouter, Path, HTTPException, status
from models.carts import Cart

cart_router = APIRouter()

carts = []

@cart_router.get("/carts", status_code=200)
async def get_carts() -> dict:
    return {
        "carts": carts
    }

@cart_router.post("/carts", status_code=201)
async def add_cart(cart: Cart) -> dict:
    carts.append(cart)
    return {
        "message": "Cart created successfully"
    }


@cart_router.get("/carts/{cart_id}", status_code=200)
async def get_cart() -> dict:
    return {
        "cart": cart
    }
    

@cart_router.put("/carts/{cart_id}", status_code=200)
async def update_cart(cart_id: int, updated_cart: Cart) -> dict:
    return {
        "message": "Cart updated successfully"
    }
    

@cart_router.delete("/carts/{cart_id}")
async def delete_cart(cart_id: int) -> dict:
    return {
        "message": "Cart deleted successfully"
    }

