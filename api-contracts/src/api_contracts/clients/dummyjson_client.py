import httpx

from api_contracts.config import Settings


class DummyJsonClient:
    def __init__(self, settings: Settings) -> None:
        self._client = httpx.Client(
            base_url=settings.base_url,
            timeout=settings.timeout_seconds,
            headers={"Accept": "application/json"},
        )

    def close(self) -> None:
        self._client.close()

    def get_products(self) -> httpx.Response:
        return self._client.get("/products")

    def get_product_by_id(self, product_id: int) -> httpx.Response:
        return self._client.get(f"/products/{product_id}")
