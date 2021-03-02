def say_hello(k, c):
    price = 0
    purchases = 0
    purchase_increse = 0
    c.sort()
    for current_flower in range(len(c) - 1, -1, -1):
        price += (1 + purchase_increse) * c[current_flower]
        purchases += 1
        if purchases % k == 0:
            purchases = 0
            purchase_increse += 1

    return price


print(say_hello(3, [1, 2, 3, 4]))
print(say_hello(3, [1, 3, 5, 7, 9]))
