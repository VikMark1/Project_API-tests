import os
from utils.base_session import BaseSession


def petstore() -> BaseSession:
    api_url = os.getenv('api_url')
    return BaseSession(base_url=api_url)