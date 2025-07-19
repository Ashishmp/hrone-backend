from database.mongoDb_Handler import order_collection, product_collection
from bson import ObjectId

def create_order(data):
    for item in data["items"]:
        item["productId"] = ObjectId(item["productId"])  # convert string to ObjectId
    result = order_collection.insert_one(data)
    return str(result.inserted_id)

def list_orders_by_user(user_id: str, limit: int = 10, offset: int = 0):
    pipeline = [
        {"$match": {"userId": user_id}},
        {"$unwind": "$items"},
        {
            "$lookup": {
                "from": "products",
                "localField": "items.productId",
                "foreignField": "_id",
                "as": "product_info"
            }
        },
        {"$unwind": {"path": "$product_info", "preserveNullAndEmptyArrays": False}},
        {
            "$group": {
                "_id": "$_id",
                "items": {
                    "$push": {
                        "productDetails": {
                            "id": {"$toString": "$product_info._id"},
                            "name": "$product_info.name"
                        },
                        "qty": "$items.qty"
                    }
                },
                "total": {"$sum": {"$multiply": ["$items.qty", "$product_info.price"]}}
            }
        },
        {
            "$project": {
                "id": {"$toString": "$_id"},
                "items": 1,
                "total": 1
            }
        },
        {"$skip": offset},
        {"$limit": limit}
    ]

    return list(order_collection.aggregate(pipeline))
