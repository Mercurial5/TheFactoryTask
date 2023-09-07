import uuid
from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models


class UserBotToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4)
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)
    chat_id = models.BigIntegerField(blank=True, null=True)


class Message(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, db_index=True)
    chat_id = models.BigIntegerField(db_index=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
