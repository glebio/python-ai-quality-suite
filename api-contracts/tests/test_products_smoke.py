import pytest

from api_contracts.clients import DummyJsonClient
from api_contracts.models.product import Product, ProductsResponse

pytestmark = [pytest.mark.external, pytest.mark.smoke]


def test_get_products_smoke(dummyjson_client: DummyJsonClient) -> None:
    response = dummyjson_client.get_products()

    assert response.status_code == 200, response.text

    products_response = ProductsResponse.model_validate(response.json())

    assert products_response.products


def test_get_product_by_id_smoke(dummyjson_client: DummyJsonClient) -> None:
    response = dummyjson_client.get_product_by_id(1)

    assert response.status_code == 200, response.text

    product = Product.model_validate(response.json())

    assert product.id == 1
    assert product.title
