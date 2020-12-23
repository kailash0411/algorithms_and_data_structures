# Uses python3
import sys


def get_fib(m, n):
    previous = 0
    current = 1
    a = 0
    b = 0
    for index in range(2, n+1):
        previous, current = current, (previous + current) % 10
        if index == m:
            a = current
    b = current
    return a, b


def get_fibonacci_last_digit_naive(n):

    if n == 0 or n == 1:
        return n
    m = n % 60
    n = (n+1) % 60

    a, b = get_fib(m, n)

    return (a * b) % 10


if __name__ == '__main__':

    n = int(input())
    print(get_fibonacci_last_digit_naive(n))

