from bitly import celery_app

from .utils import send_telegram_message


@celery_app.task
def send_telegram_message_task(message: str) -> None:
    send_telegram_message(message)
