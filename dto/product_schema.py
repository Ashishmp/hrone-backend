from pydantic import BaseModel
from typing import List

class SizeEntry(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[SizeEntry]

class ProductId(BaseModel):
    id: str

class ProductListItem(BaseModel):
    id: str
    name: str
    price: float

class PageInfo(BaseModel):
    next: int
    limit: int
    previous: int

class ProductListResponse(BaseModel):
    data: List[ProductListItem]
    page: PageInfo
