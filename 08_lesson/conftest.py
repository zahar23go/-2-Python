import pytest
import os

@pytest.fixture(scope="session")
def base_url():
    return "https://yougile.com/api-v2"

@pytest.fixture(scope="session")
def auth_token():
    token = os.getenv('YOUGILE_TOKEN')
    if not token:
        pytest.skip("YOUGILE_TOKEN не установлен")
    return token
