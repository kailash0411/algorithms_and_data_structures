# Uses python3
import sys

def gcd_naive(a, b):
    if a < b:
        a, b = b, a
    while b:
        t = b
        b = a % b
        a = t

    return a

if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())
    if a == b:
        print(a)
    elif a == 1 or b == 1:
        print(1)
    else:
        print(gcd_naive(a, b))
