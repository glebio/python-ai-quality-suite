from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(extra="ignore", strict=True)

    id: int
    title: str
    price: float
    rating: float
    stock: int


class ProductsResponse(BaseModel):
    model_config = ConfigDict(extra="ignore", strict=True)

    products: list[Product]
    total: int
    skip: int
    limit: int
