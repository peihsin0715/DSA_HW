def maximum_value(expression):
    n = len(expression)
    digit = [int(expression[i]) for i in range(0, n, 2)]
    operation = [expression[i] for i in range(1, n, 2)]

    m = [[0]* (len(digit) + 1) for _ in range(len(digit) + 1)]
    M = [[0]* (len(digit) + 1) for _ in range(len(digit) + 1)]
    for i in range(1, len(digit) + 1):
        m[i][i] = digit[i - 1]
        M[i][i] = digit[i - 1]
    for s in range(1, len(digit)):
        for i in range(1, len(digit) + 1 - s):
            j = i + s
            minimum = float("+inf")
            maximum = float("-inf")
            for k in range(i, j):
                a = evaluate(M[i][k], M[k+1][j], operation[k - 1])
                b = evaluate(M[i][k], m[k+1][j], operation[k - 1])
                c = evaluate(m[i][k], M[k+1][j], operation[k - 1])
                d = evaluate(m[i][k], m[k+1][j], operation[k - 1])
                minimum = min(minimum, a, b, c, d)
                maximum = max(maximum, a, b, c, d)
            m[i][j] = minimum
            M[i][j] = maximum
    return M[1][len(digit)]


def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


if __name__ == "__main__":
    print(maximum_value(input()))
