def change(money):
    coins = (1, 3, 4)
    min_coins = [float("inf")] * (money + 1)
    min_coins[0] = 0

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                num_coins = min_coins[i - coin] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins

    return min_coins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
