from typing import Protocol

from django.contrib.auth import get_user_model

from .models import UserBotToken

User = get_user_model()


class UserBotTokenRepositoriesInterface(Protocol):

    @staticmethod
    def generate_token(user: User) -> UserBotToken: ...

    @staticmethod
    def get_token_by_token(token: str) -> UserBotToken | None: ...

    @staticmethod
    def get_token_by_user(user: User) -> UserBotToken | None: ...

    @staticmethod
    def bind_token_to_chat_id(token: UserBotToken, chat_id: int) -> None: ...


class UserBotTokenRepository:

    @staticmethod
    def generate_token(user: User) -> UserBotToken:
        token, _ = UserBotToken.objects.get_or_create(user=user)
        return token

    @staticmethod
    def get_token_by_token(token: str) -> UserBotToken | None:
        try:
            return UserBotToken.objects.get(token=token)
        except UserBotToken.DoesNotExist:
            return None

    @staticmethod
    def get_token_by_user(user: User) -> UserBotToken | None:
        try:
            return UserBotToken.objects.get(user=user)
        except UserBotToken.DoesNotExist:
            return None

    @staticmethod
    def bind_token_to_chat_id(token: UserBotToken, chat_id: int) -> None:
        token.chat_id = chat_id
        token.save()
