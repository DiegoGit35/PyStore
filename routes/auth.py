from fastapi import APIRouter, HTTPException, status
from models import AuthDetails

auth_router = APIRouter()

users = []

@auth_router.post("/signup", status_code=201)
async def signup(auth_details: AuthDetails) -> dict:
    # Aquí deberías añadir lógica para registrar al usuario
    return {
        "message": "User signed up successfully"
    }

@auth_router.post("/login", status_code=200)
async def login(auth_details: AuthDetails) -> dict:
    # Aquí deberías añadir lógica para autenticar al usuario
    return {
        "message": "User logged in successfully"
    }

@auth_router.post("/refresh", status_code=200)
async def refresh_token() -> dict:
    # Aquí deberías añadir lógica para refrescar el token de acceso
    return {
        "message": "Access token refreshed successfully"
    }
