# Uses python3
import sys


def get_pisano_period(k):
    previous, current = 0, 1
    for i in range(0, k*k):
        previous, current = current, (previous + current) % k
        if previous == 0 and current == 1:
            return i+1


def get_fibonacci_mod(n, k):
    pisano_period = get_pisano_period(k)
    n = n % pisano_period
    if n == 1:
        return 1
    if n == 0:
        return 0
    previous, current = 0, 1
    for i in range(n-1):
        previous, current = current, (previous+current) % k

    return (current % k)

if __name__ == '__main__':
    input = input()
    n, k = map(int, input.split())
    print(get_fibonacci_mod(n, k))
