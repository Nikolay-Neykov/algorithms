def say_hello(k, arr):
    min = float('inf')
    arr.sort()
    l = len(arr)
    i = 0
    j = k - 1
    while j < l:
        new_min = arr[j] - arr[i]
        min = min if min < new_min else new_min
        j += 1
        i += 1

    return min


print(say_hello(3, [10, 100, 300, 200, 1000, 20, 30]))
print(say_hello(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))
