from api_contracts.clients import DummyJsonClient


def test_get_products_smoke(dummyjson_client: DummyJsonClient) -> None:
    response = dummyjson_client.get_products()

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0


def test_get_product_by_id_smoke(dummyjson_client: DummyJsonClient) -> None:
    response = dummyjson_client.get_product_by_id(1)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert isinstance(data["title"], str)
    assert data["title"] != ""
