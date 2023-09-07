from rest_framework import serializers

from .models import Message


class SendMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=4000)


class GetMessagesSerializer(serializers.Serializer):
    chat_id = serializers.IntegerField(required=False, allow_null=True)


class RetrieveMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
