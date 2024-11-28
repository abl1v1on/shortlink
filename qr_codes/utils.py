import qrcode
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
UPLOAD_TO = BASE_DIR / 'media' / 'qr_codes'


def create_qr(url: str, file_name: str) -> None:
    img = qrcode.make(url)
    file_path = UPLOAD_TO / f'{file_name}.jpg'
    img.save(file_path)
    return f'qr_codes/{file_name}.jpg'
