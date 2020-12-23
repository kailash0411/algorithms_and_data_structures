# Uses python3
import sys


def recursive_binary_search(left, right, x):
    if left <= right:
        mid = left + int((right - left) / 2)
        if a[mid] == x:
            return mid

        elif a[mid] < x:
            left = mid + 1
            return recursive_binary_search(left, right, x)
        else:
            right = mid - 1
            return recursive_binary_search(left, right, x)

    return -1


def iterative_binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(iterative_binary_search(a, x), end=' ')
        # print(linear_search(a, x), end=' ')
