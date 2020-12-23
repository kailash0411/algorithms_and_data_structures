# Uses python3
import sys

def optimal_weight(W, w):

    value = [[0 for x in range(W+1)] for y in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for weight in range(1, W+1):
            value[i][weight] = value[i-1][weight]
            if w[i-1] <= weight:
                val = value[i-1][weight - w[i-1]] + w[i-1]
                if val > value[i][weight]:
                    value[i][weight] = val
    return value[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
