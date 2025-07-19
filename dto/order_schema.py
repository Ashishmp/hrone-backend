from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    productId: str
    qty: int

class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItem]

class ProductBrief(BaseModel):
    id: str
    name: str

class OrderItemOut(BaseModel):
    productDetails: ProductBrief
    qty: int

class OrderOut(BaseModel):
    id: str
    items: List[OrderItemOut]
    total: float

class PageInfo(BaseModel):
    next: int
    limit: int
    previous: int

class OrderListResponse(BaseModel):
    data: List[OrderOut]
    page: PageInfo

class OrderCreateResponse(BaseModel):
    id: str

