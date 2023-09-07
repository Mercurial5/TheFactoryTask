from typing import Protocol

from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from .models import UserBotToken, Message
from .repositories import UserBotTokenRepository, UserBotTokenRepositoriesInterface, MessageRepositoriesInterface, \
    MessageRepository

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


class MessageServicesInterface(Protocol):

    def create_message(self, user: User, chat_id: int, message: str) -> Message: ...

    def get_messages(self, user: User, chat_id: int | None) -> QuerySet[Message]: ...


class MessageService:
    repository: MessageRepositoriesInterface = MessageRepository()

    def create_message(self, user: User, chat_id: int, message: str) -> Message:
        return self.repository.create_message(user, chat_id, message)

    def get_messages(self, user: User, chat_id: int | None) -> QuerySet[Message]:
        return self.repository.get_messages(user, chat_id)
