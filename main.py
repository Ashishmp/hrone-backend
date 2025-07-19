from fastapi import FastAPI
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
import os
from dto.order_schema import OrderCreate, OrderOut, OrderListResponse, OrderCreateResponse
from models.order import create_order as db_create_order, list_orders_by_user as db_list_orders
from dto.product_schema import ProductCreate, ProductId,  ProductListResponse
from models.product import create_product as db_create_product, list_products as db_list_products


# FastAPI app instance
app = FastAPI()

# CORS for frontend (adjust origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Product APIs
# -------------------------

@app.post("/products", response_model=ProductId, status_code=201)
def create_product_route(product: ProductCreate):
    product_id = db_create_product(product.dict())
    return {
        "id": product_id,
        "name": product.name,
        "price": product.price
    }

@app.get("/products", response_model=ProductListResponse, status_code=200)
def list_products_route(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    products = db_list_products(name, size, limit, offset)

    return {
        "data": products,
        "page": {
            "next": offset + limit,
            "limit": len(products),
            "previous": max(offset - limit, 0)
        }
    }

# -------------------------
# Order APIs
# -------------------------

@app.post("/orders", response_model=OrderCreateResponse, status_code=201)
def create_order_route(order: OrderCreate):
    order_id = db_create_order(order.dict())
    return {"id": order_id}

@app.get("/orders/{user_id}", response_model=OrderListResponse, status_code=200)
def list_orders_route(user_id: str, limit: int = 10, offset: int = 0):
    orders = db_list_orders(user_id, limit, offset)
    return {
        "data": orders,
        "page": {
            "next": offset + limit,
            "limit": len(orders),
            "previous": max(offset - limit, 0)
        }
    }
