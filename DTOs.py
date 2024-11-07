from pydantic import BaseModel


class ProductRequest(BaseModel):
    name: str
    description: str
    qtd: int
    price: float
    has_discount: bool
    discount: float
    image_url: str


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    qtd: int
    price: float
    has_discount: bool
    discount: float
    image_url: str
