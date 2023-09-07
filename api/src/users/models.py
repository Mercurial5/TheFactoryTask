from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=64)
    token = models.UUIDField(blank=True, null=True)

    EMAIL_FIELD = 'username'
    REQUIRED_FIELDS = ['name']
