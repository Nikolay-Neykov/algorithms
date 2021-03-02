def say_hello():
    sum = 0
    for i in range(1000):
        sum += i if (i % 5 == 0) or (i % 3 == 0) else 0
        print(f'sum: {sum}, i: {i}, 5: {i % 5}, 3: {i % 3}')
    return sum


print(say_hello())
