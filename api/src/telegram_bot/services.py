from typing import Protocol

from django.contrib.auth import get_user_model

from .models import UserBotToken
from .repositories import UserBotTokenRepository, UserBotTokenRepositoriesInterface

User = get_user_model()


class UserBotTokenServicesInterface(Protocol):

    def generate_token(self, user: User) -> UserBotToken: ...

    def get_token_by_token(self, token: str) -> UserBotToken | None: ...

    def get_token_by_user(self, user: User) -> UserBotToken | None: ...

    def bind_token_to_chat_id(self, token: UserBotToken, chat_id: int) -> None: ...


class UserBotTokenService:
    repository: UserBotTokenRepositoriesInterface = UserBotTokenRepository()

    def generate_token(self, user: User) -> UserBotToken:
        return self.repository.generate_token(user)

    def get_token_by_token(self, token: str) -> UserBotToken | None:
        return self.repository.get_token_by_token(token)

    def get_token_by_user(self, user: User) -> UserBotToken | None:
        return self.repository.get_token_by_user(user)

    def bind_token_to_chat_id(self, token: UserBotToken, chat_id: int) -> None:
        return self.repository.bind_token_to_chat_id(token, chat_id)
