from typing import Protocol, OrderedDict

from django.db import transaction
from django.db.models import QuerySet
from rest_framework.authtoken.models import Token

from . import models


class UserRepositoriesInterface(Protocol):
    @staticmethod
    def create_user(data: OrderedDict) -> Token: ...

    @staticmethod
    def get_users() -> QuerySet[models.User]: ...


class UserRepository:
    @staticmethod
    @transaction.atomic
    def create_user(data: OrderedDict) -> Token:
        user = models.User.objects.create_user(**data)
        token = Token.objects.create(user=user)
        return token

    @staticmethod
    def get_users() -> QuerySet[models.User]:
        return models.User.objects.all()
