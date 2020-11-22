#!/usr/bin/env python3

def recursion(arr, index):
    if index == len(arr):
        print(f'{arr} for index {index}')
        return

    for x in range(2):
        arr[index] = x
        recursion(arr, index + 1)


def main():
    arr = [0, 0, 0, 0, 0, 0, 0, 0]
    recursion(arr, 0)


if __name__ == '__main__':
    main()
