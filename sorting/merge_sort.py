def merge_sort(arr):
    result = []
    # 7
    length = len(arr)
    if length <= 1:
        #         print(f'floor of {arr}')
        return arr
    # 4
    mid = length // 2

#     print(f'length {length}')
#     print(f'mid {mid}')
    # 0,1,2,3
    left = merge_sort(arr[:mid])
    # 4,5,6
    right = merge_sort(arr[mid:])

#     print(f'left {left}')
#     print(f'right {right}')

    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


result = merge_sort([38, 27, 43, 3, 9, 82, 10])
if not result == [3, 9, 10, 27, 38, 43, 82]:
    raise Exception("common case failed")

print(f'Success common case: {result}')

result = merge_sort([1, 2, 3, 4, 5, 6, 7])
if not result == [1, 2, 3, 4, 5, 6, 7]:
    raise Exception("ordered case failed")

print(f'Success ordered case: {result}')
