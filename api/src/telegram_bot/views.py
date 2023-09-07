from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from telegram_bot.serializers import MessageSerializer
from telegram_bot.services import UserBotTokenService, UserBotTokenServicesInterface
from telegram_bot.telegram_bot import bot


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def generate_token(request: Request) -> Response:
    service: UserBotTokenServicesInterface = UserBotTokenService()

    token = service.generate_token(request.user)

    return Response({'token': token.token}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def send(request: Request) -> Response:
    serializer = MessageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    service: UserBotTokenServicesInterface = UserBotTokenService()

    token = service.get_token_by_user(user=request.user)
    if not token:
        return Response({'detail': 'You did not generated token!'}, status=status.HTTP_400_BAD_REQUEST)

    if not token.chat_id:
        return Response({'detail': 'You did not bind any chat!'}, status=status.HTTP_400_BAD_REQUEST)

    bot.send_message(token.chat_id, serializer.validated_data['message'])

    return Response({}, status=status.HTTP_204_NO_CONTENT)
