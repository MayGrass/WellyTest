# python 3.10.2


import json


userIds = ["U01", "U02", "U03"]
orderIds = ["T01", "T02", "T03", "T04"]
userOrders = [
    {"userId": "U01", "orderIds": ["T01", "T02"]},
    {"userId": "U02", "orderIds": []},
    {"userId": "U03", "orderIds": ["T03"]},
]
userData = {"U01": "Tom", "U02": "Sam", "U03": "John"}
orderData = {
    "T01": {"name": "A", "price": 499},
    "T02": {"name": "B", "price": 599},
    "T03": {"name": "C", "price": 699},
    "T04": {"name": "D", "price": 799},
}

new_userOrders = {userOrder["userId"]: userOrder["orderIds"] for userOrder in userOrders}
print(new_userOrders)

output = [
    {
        "user": {"id": userId, "name": userData.get(userId)},
        "orders": [{"id": orderId} | orderData[orderId] for orderId in new_userOrders[userId]],
    }
    for userId in userIds
]
print(json.dumps(output, indent=2))
