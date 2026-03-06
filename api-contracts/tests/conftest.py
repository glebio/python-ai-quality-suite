from collections.abc import Generator

import pytest

from api_contracts.clients import DummyJsonClient
from api_contracts.config import get_settings


@pytest.fixture
def dummyjson_client() -> Generator[DummyJsonClient, None, None]:
    client = DummyJsonClient(get_settings())
    try:
        yield client
    finally:
        client.close()
