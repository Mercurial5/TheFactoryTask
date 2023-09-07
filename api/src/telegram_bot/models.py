import uuid

from django.contrib.auth import get_user_model
from django.db import models


class UserBotToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4)
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)
    chat_id = models.BigIntegerField(blank=True, null=True)
