# Uses python3
import sys


def get_fib_n(n):

    previous = 0
    current = 1
    for index in range(2, n+3):
        previous, current = current, (previous + current)%10

    return current

def get_fib_m(m):

    previous = 0
    current = 1
    for index in range(2, m+3):
        previous, current = current, (previous + current)%10

    return current
def get_fibonacci_last_digit_naive(m, n):

    a = get_fib_n(n % 60) - get_fib_m( (m-1)% 60)

    return a%10


if __name__ == '__main__':

    m, n = map(int, input().split())
    print(get_fibonacci_last_digit_naive(m, n))

