import os
import pytest
from dotenv import load_dotenv
from utils.base_session import BaseSession


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def petstore_session():
    api_url = os.getenv('api_url')
    with BaseSession(base_url=api_url) as session:
        yield session
