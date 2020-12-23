# Uses python3
import sys

def min_ops(n):
    result = [0]* (n+1)
    for i in range(2 , n+1):
        min1 = result[i-1]
        min2 = n
        min3 = n
        if i % 2 == 0:
            min2 = result[i // 2]
        if i % 3 == 0:
            min3 = result[i // 3]
        min_op = min(min1, min2, min3)
        result[i] = min_op + 1
    return result



def optimal_sequence(n):
    if n == 1:
        return [1]
    ops = min_ops(n)
    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n-1
        elif n % 2 == 0 and n % 3 == 0:
            n = n // 3
        elif n % 3 == 0:
            if ops[n-1] < ops[ n // 3]:
                n = n-1
            else:
                n = n // 3
        elif n % 2 == 0:
            if ops[n - 1] < ops[n // 2]:
                n = n - 1
            else:
                n = n // 2

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
