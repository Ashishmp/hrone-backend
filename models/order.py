from database import order_collection, product_collection
from bson import ObjectId

def create_order(data):
    result = order_collection.insert_one(data)
    return str(result.inserted_id)

def list_orders_by_user(user_id, limit=10, offset=0):
    query = {"userId": user_id}
    cursor = order_collection.find(query).skip(offset).limit(limit)

    orders = []
    for order in cursor:
        total = 0.0
        items_out = []

        for item in order["items"]:
            product = product_collection.find_one({"_id": ObjectId(item["productId"])})
            if product:
                product_info = {
                    "id": str(product["_id"]),
                    "name": product["name"]
                }
                items_out.append({
                    "productDetails": product_info,
                    "qty": item["qty"]
                })
                total += product["price"] * item["qty"]

        orders.append({
            "id": str(order["_id"]),
            "items": items_out,
            "total": round(total, 2)
        })

    return orders
