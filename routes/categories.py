from fastapi import APIRouter, Path, HTTPException, status
from models.categories import Categories

category_router = APIRouter()

categories = []

@category_router.get("/categories", status_code=200)
async def get_categories() -> dict:
    return {
        "categories": categories
    }

@category_router.post("/categories", status_code=201)
async def add_category(categories: Categories) -> dict:
    categories.append(category)
    return {
        "message": "Category created successfully"
    }

@category_router.get("/categories/{category_id}", status_code=200)
async def get_category() -> dict:
    return {
        "category": category
    }


@category_router.put("/categories/{category_id}", status_code=200)
async def update_category(category_id: int, updated_category: Categories) -> dict:
    return {  
        "message": "Category updated successfully"
    }
    

@category_router.delete("/categories/{category_id}")
async def delete_category(category_id: int) -> dict:
    return {
            "message": "Category deleted successfully"
    }
    
    