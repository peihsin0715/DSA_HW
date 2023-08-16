def lcs2(first_sequence, second_sequence, third_sequence):
    m = len(first_sequence)
    n = len(second_sequence)
    p = len(third_sequence)
    T = [[[float('-inf')] * (p + 1) for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            T[i][j][0] = 0
    for i in range(m + 1):
        for k in range(p + 1):
            T[i][0][k] = 0
    for j in range(n + 1):
        for k in range(p + 1):
            T[0][j][k] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, p + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]:
                    T[i][j][k] = T[i - 1][j - 1][k - 1] + 1
                else:
                    T[i][j][k] = max(T[i - 1][j][k], T[i][j - 1][k], T[i][j][k - 1])

    return T[m][n][p]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    p = int(input())
    c = list(map(int, input().split()))
    assert len(c) == p

    print(lcs2(a, b, c))
