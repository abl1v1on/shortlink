import qrcode
from bitly import settings
from pathlib import Path


UPLOAD_TO = Path(settings.BASE_DIR) / 'media' / 'qr_codes'


def create_qr(url: str, file_name: str) -> str:
    img = qrcode.make(url)
    file_path = UPLOAD_TO / f'{file_name}.jpg'
    img.save(file_path)
    return f'qr_codes/{file_name}.jpg'


def delete_qr():
    pass
