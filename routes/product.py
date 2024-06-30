from fastapi import APIRouter, Path, HTTPException, status
from models.product import Product

product_router = APIRouter()

products = []

@product_router.get("/products", status_code=200)
async def get_products() -> dict:
    return {
        "products": products
    }


@product_router.post("/products", status_code=201)
async def add_product(product: Product) -> dict:
    products.append(product)
    return {
        "message": "Product created successfully"
    }


@product_router.get("/products/{product_id}", status_code=200)
async def get_product() -> dict:
    return {
            "product": product
    }


@product_router.put("/products/{product_id}", status_code=200)
async def update_product(product_id: int, updated_product: Product) -> dict:
    return {
            "message": "Product updated successfully"
    }


@product_router.delete("/products/{product_id}")
async def delete_product(product_id: int) -> dict:
    return {
            "message": "Product deleted successfully"
    }