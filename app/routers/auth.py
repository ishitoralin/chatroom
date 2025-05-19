from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

from app.models.auth import auths

router = APIRouter()

@router.post("/login", response_model=dict)
async def post_login(request: Request):
    data = await request.json()
    result = auths.verify_password(data["username"], data["password"])
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )


    return {"message": data}