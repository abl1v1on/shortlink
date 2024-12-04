import os
import requests
from requests import Response
from dotenv import load_dotenv
from uuid import uuid4
from django.db.models import QuerySet
from django.contrib.auth.models import User

from .models import Link


load_dotenv()

def gen_short_link() -> str:
    return str(uuid4()).split('-')[0]


def get_user_links(user: User) -> QuerySet[Link]:
    return user.links.all().prefetch_related('tags', 'awards')


def send_telegram_message(message: str) -> Response:
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response
