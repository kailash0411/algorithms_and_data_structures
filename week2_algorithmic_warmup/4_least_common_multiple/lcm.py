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
def lcm_naive(a,b):
    gcd = gcd_naive(a,b)
    return int(a*(b/gcd))


if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())
    if a == b:
        print(a)
    elif a == 1 or b == 1:
        print(a*b)
    else:
        print(lcm_naive(a, b))

