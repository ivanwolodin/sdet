from abc import ABC, abstractmethod

from app.schemas.auth import LoginData


class AuthServiceInterface(ABC):
    @abstractmethod
    def authenticate_user(self, login_data: LoginData) -> bool:
        pass
