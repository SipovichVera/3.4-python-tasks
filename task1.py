def fibonacci(position):
    item_1 = 0
    item_2 = 1
    for i in range(position):
        yield item_1 + item_2
        item_1, item_2 = item_2, item_2 + item_1

for item in fibonacci(10):
    print(item)