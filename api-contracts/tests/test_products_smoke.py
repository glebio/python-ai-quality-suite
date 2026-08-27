from api_contracts.clients import DummyJsonClient
from api_contracts.models.product import Product


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
    product = Product.model_validate(data)
    assert product.id == 1
