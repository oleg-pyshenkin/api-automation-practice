import pytest
from api_client import PostClient
from config import BASE_URL

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def post_client(base_url):
    return PostClient(base_url)