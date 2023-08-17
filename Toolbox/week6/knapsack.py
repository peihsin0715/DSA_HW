def maximum_gold(capacity, weights):
    n = len(weights)
    T = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            T[i][w] = T[i - 1][w]
            if w >= weights[i - 1]:
                value = T[i - 1][w - weights[i - 1]] + weights[i - 1]
                if value > T[i][w]:
                    T[i][w] = value

    return T[n][capacity]


if __name__ == '__main__':
    input_capacity, n = map(int, input().split())
    input_weights = list(map(int, input().split()))
    assert len(input_weights) == n

    max_value = maximum_gold(input_capacity, input_weights)
    print(max_value)
