# Uses python3
import sys
import itertools

def partition3(W, n, w):
    value = [[0 for x in range(W+1)] for y in range(n+1)]
    count = 0
    for i in range(1, n + 1):
        for weight in range(1, W + 1):
            value[i][weight] = value[i - 1][weight]
            if w[i - 1] <= weight:
                val = value[i - 1][weight - w[i - 1]] + w[i - 1]
                if val > value[i][weight]:
                    value[i][weight] = val
            if value[i][weight] == W:
                count += 1
    if count < 3:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    if n < 3:
        print(0)
    elif sum(A) % 3 != 0:
        print(0)
    else:
        print(partition3(sum(A)//3, n,  A))

