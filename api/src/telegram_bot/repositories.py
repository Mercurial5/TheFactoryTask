from typing import Protocol

from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from .models import UserBotToken, Message

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


class MessageRepositoriesInterface(Protocol):

    @staticmethod
    def create_message(user: User, chat_id: int, message: str) -> Message: ...

    @staticmethod
    def get_messages(user: User, chat_id: int | None) -> QuerySet[Message]: ...


class MessageRepository:

    @staticmethod
    def create_message(user: User, chat_id: int, message: str) -> Message:
        return Message.objects.create(user=user, chat_id=chat_id, message=message)

    @staticmethod
    def get_messages(user: User, chat_id: int | None) -> QuerySet[Message]:
        query = Message.objects.filter(user=user)

        if chat_id:
            query = query.filter(chat_id=chat_id)

        return query.all()
