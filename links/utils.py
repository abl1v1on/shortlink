from uuid import uuid4


def gen_short_link() -> str:
    return str(uuid4()).split('-')[0]
