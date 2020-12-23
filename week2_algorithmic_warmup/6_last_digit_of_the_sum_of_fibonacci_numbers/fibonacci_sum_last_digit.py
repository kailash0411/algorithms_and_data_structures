# Uses python3
import sys


def get_fib(n):
    previous = 0
    current = 1
    for index in range(2, n+3):
        previous, current = current, (previous + current) % 10
    return current


def get_fibonacci_last_digit_naive(n):
    if n == 0 or n == 1:
        return n

    a = get_fib(n % 60)

    return (a - 1) % 10


if __name__ == '__main__':

    n = int(input())
    print(get_fibonacci_last_digit_naive(n))

