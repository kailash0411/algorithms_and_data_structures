# Uses python3


def calculate_10_coins(m):
    res = m % 10
    coins = int(m / 10)
    return res, coins

def calculate_5_coins(m):
    res = m % 5
    coins = int(m/5)
    return res, coins

def get_change(m):
    sum = 0
    while m >= 5:
        if m >=10:
            m, coins = calculate_10_coins(m)

        else:
            m, coins = calculate_5_coins(m)

        sum = sum + coins

    return sum + m


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
