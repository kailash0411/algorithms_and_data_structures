# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    a = [0, 1, 1]
    for index in range(3, n+1):
        a.append(a[index-1] + a[index-2])

    return a[-1]

n = int(input())
print(calc_fib(n))
