def lcs2(first_sequence, second_sequence):
    m = len(first_sequence)
    n = len(second_sequence)
    T = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        T[i][0] = 0
    for j in range(n + 1):
        T[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

    return T[m][n]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
