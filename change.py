def change(money):
    coins = [10, 5, 1]
    total_coins = 0
    for coin in coins:
        if money // coin > 0:
            total_coins += money // coin
            money -= (money // coin) * coin
    return total_coins

if __name__ == '__main__':
    m = int(input())
    print(change(m))
