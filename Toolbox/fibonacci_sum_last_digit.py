def get_last_digit_fibonacci(n):
    F = [0, 1]
    last = [0, 1]
    for i in range(2, 60):
        F.append(F[i - 1] + F[i - 2])
        last.append(int(str(F[i])[-1]))

    result = 2 * last[n % 60] + last[(n - 1) % 60] - 1
    return result % 10

if __name__ == '__main__':
    n = int(input())
    result = get_last_digit_fibonacci(n)
    print(result)
