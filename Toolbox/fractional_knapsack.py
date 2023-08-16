from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    value_per_weight = [v / w for v, w in zip(values, weights)] 
    while capacity > 0 and len(value_per_weight) > 0:
        max_value_per_weight = max(value_per_weight)
        max_value_index = value_per_weight.index(max_value_per_weight)
        if weights[max_value_index] <= capacity:
            value += values[max_value_index]
            capacity -= weights[max_value_index]
            value_per_weight.pop(max_value_index)
            weights.pop(max_value_index)
            values.pop(max_value_index)
        else:
            value += capacity * max_value_per_weight
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
