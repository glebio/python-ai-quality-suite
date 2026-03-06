from api_contracts.clients import DummyJsonClient
from api_contracts.config import get_settings


def test_get_products_smoke() -> None:
    client = DummyJsonClient(get_settings())

    try:
        response = client.get_products()

        assert response.status_code == 200

        data = response.json()

        assert "products" in data
        assert isinstance(data["products"], list)
        assert len(data["products"]) > 0
    finally:
        client.close()
