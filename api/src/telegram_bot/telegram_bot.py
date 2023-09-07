import telebot
from django.conf import settings
from telebot import TeleBot

from telegram_bot.services import UserBotTokenServicesInterface, UserBotTokenService

bot = TeleBot(settings.TELEGRAM_BOT_TOKEN)


@bot.message_handler(func=lambda message: message.text.startswith('register '))
def start(message: telebot.types.Message):
    token = message.text.replace('register ', '')

    service: UserBotTokenServicesInterface = UserBotTokenService()

    token = service.get_token_by_token(token)
    if not token:
        bot.send_message(message.chat.id, 'Token does not exists!')
        return

    service.bind_token_to_chat_id(token, message.chat.id)

    bot.send_message(message.chat.id, 'Binded your token to this chat!')
