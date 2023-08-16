def max_dot_product(first_sequence, second_sequence):
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)
    max_product = sum(first_sequence[i] * second_sequence[i] for i in range(len(first_sequence)))
    return max_product

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
