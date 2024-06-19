from django.core.management.base import BaseCommand

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import environ
from bot.utils import generate_code
from django.core.cache import cache

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env('.env')

TOKEN = env.str('TOKEN')

bot = telebot.TeleBot(token=TOKEN)


def get_contact_button():
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    contact = KeyboardButton(text="📱Kontaktni yuborish", request_contact=True)
    button.add(contact)
    return button


@bot.message_handler(commands=['start', 'login'])
def send_welcome(message):
    msg = (f"Salom Doniyor 👋\n"
           f"@dj_auth401_bot'ning rasmiy botiga xush kelibsiz\n\n"
           f"⬇️ Kontaktingizni yuboring (tugmani bosib)")
    bot.send_message(chat_id=message.chat.id, text=msg, reply_markup=get_contact_button())


@bot.message_handler(content_types=["contact"])
def check_contact(message):
    if message.from_user.id == message.contact.user_id:
        code = generate_code()
        user_id = message.from_user.id
        cache.set(code, user_id, timeout=60)
        msg = (f"🔐 Kodingiz: \n"
               f"{code}")
        bot.send_message(message.chat.id, text=msg, reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id, text="🔑 Yangi kod olish uchun /login ni bosing.")

    else:
        bot.send_message(message.chat.id, text="🖕Shahsiy kontaktingizni yuboring")


class Command(BaseCommand):

    def handle(self, *args, **options):
        bot.polling()
