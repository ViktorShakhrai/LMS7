# Input data:
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock.
# Створіть функцію, яка бере в якості вхідних даних два dicts із згаданою вище структурою, потім обчислює та повертає загальну ціну акцій.

def calculate(stock: dict, prices: dict):
    total_price = {}
    for st in stock:
        if st in prices:
            total_price[st] = stock[st] * prices[st]
    return total_price


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

z = calculate(stock, prices)
print(z)
