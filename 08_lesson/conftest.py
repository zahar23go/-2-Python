import pytest
import os

BASE_URL = "https://yougile.com/api-v2"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def auth_token():
    token = os.getenv("YOUGILE_TOKEN")
    if not token:
        pytest.skip("YOUGILE_TOKEN is not set")
    return token
