# Uses python3
import sys


def get_fib(a, n):
    if (n <= 1):
        return n
    a[0] = 0
    a[1] = 1
    for index in range(2, n + 1):
        a[index] = (a[index - 1] + a[index - 2]) % 10
    return a


def get_fibonacci_last_digit_naive(n):
    if (n <= 1):
        return n
    a = [0] * 61
    a = get_fib(a, 60)
    return a[n % 60]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
