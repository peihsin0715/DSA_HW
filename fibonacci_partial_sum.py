def get_last_digit_fibonacci_cycle_length():
    F = [0, 1]
    last = [0, 1]
    for i in range(2, 60):
        F.append(F[i - 1] + F[i - 2])
        last.append(int(str(F[i])[-1]))
    return last

def calculate_last_digit_sum(m, n):
    last = get_last_digit_fibonacci_cycle_length()
    q = (n - m + 1) // 60

    total = 0
    for i in range((m + q * 60), (n + 1)):
        total = total + last[i % 60]

    return total % 10

if __name__ == '__main__':
    a = input()
    m, n = map(int, a.split())
    
    result = calculate_last_digit_sum(m, n)
    print(result)
