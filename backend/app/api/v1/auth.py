from app.auth_service.authenticator import AuthService, get_auth_service
from app.schemas.auth import LoginData
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()


@router.post('/login', status_code=status.HTTP_200_OK)
def login(
    login_data: LoginData,
    auth_service: AuthService = Depends(get_auth_service),
):
    if auth_service.authenticate_user(login_data=login_data):
        return {"res": "authorized!"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
