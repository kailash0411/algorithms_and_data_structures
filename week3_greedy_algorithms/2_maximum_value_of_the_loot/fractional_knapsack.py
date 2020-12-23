# Uses python3
import sys
from functools import reduce


def get_optimal_value(capacity, weights, values):
    value = 0
    if capacity > reduce(lambda a, b: a + b, weights):
        return reduce(lambda a, b: a + b, values)
    proportion = [float(v)/float(w) for v, w in zip(values, weights)]
    for _ in range(len(weights)+1):
        max_weight = max(proportion)
        index = proportion.index(max_weight)
        proportion[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_weight
        weights[index] -= add_capacity
        capacity -= add_capacity
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
