# Uses python3
import sys

def get_change(m):
    min_coins = [0] * (m + 1)
    min_coins[0] = 0
    changes = [1, 3, 4]
    for i in range(1, m+1):
        min_coins[i] = i
        if i == 1 or i == 3 or i == 4:
            min_coins[i] = 1
        for change in changes:
            if i > change:
                no_coins = min_coins[i-change] + 1
                if no_coins < min_coins[i]:
                    min_coins[i] = no_coins

    return min_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
