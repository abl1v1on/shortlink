from bitly import celery_app

from .utils import create_qr


@celery_app.task
def create_qr_task(url: str, file_name: str) -> str:
    return create_qr(url, file_name)
