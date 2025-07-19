from database.mongoDb_Handler import product_collection

def create_product(data):
    result = product_collection.insert_one(data)
    return str(result.inserted_id)

def list_products(name=None, size=None, limit=10, offset=0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = product_collection.find(query).skip(offset).limit(limit)
    data = []
    for prod in cursor:
        data.append({
            "id": str(prod["_id"]),
            "name": prod["name"],
            "price": prod["price"]
        })

    return data
