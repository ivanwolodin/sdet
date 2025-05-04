from functools import lru_cache
from app.core.config import config
from app.interfaces.auth_service import AuthServiceInterface
from app.schemas.auth import LoginData


class AuthService(AuthServiceInterface):
    def authenticate_user(self, login_data: LoginData):
        if login_data.login == config.USER_LOGIN and login_data.password == config.USER_PASSWORD:
            return True
        return False


@lru_cache()
def get_auth_service() -> AuthService:
    return AuthService()
