from typing import Protocol, OrderedDict

from django.db.models import QuerySet
from rest_framework.authtoken.models import Token

from . import models
from .repositories import UserRepositoriesInterface, UserRepository


class UserServicesInterface(Protocol):
    def create_user(self, data: OrderedDict) -> Token: ...

    def get_users(self) -> QuerySet[models.User]: ...


class UserService:
    repository: UserRepositoriesInterface = UserRepository()

    def create_user(self, data: OrderedDict) -> Token:
        return self.repository.create_user(data)

    def get_users(self) -> QuerySet[models.User]:
        return self.repository.get_users()
