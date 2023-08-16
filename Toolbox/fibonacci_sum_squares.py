def get_last_digit_fibonacci_cycle_length():
    F = [0, 1]
    last = [0, 1]
    for i in range(2, 60):
        F.append(F[i - 1] + F[i - 2])
        last.append(int(str(F[i])[-1]))
    return last

def calculate_last_digit_square_sum(n):
    last = get_last_digit_fibonacci_cycle_length()
    S = last[n % 60] * last[n % 60] + last[n % 60] * last[(n - 1) % 60]
    return S % 10

if __name__ == '__main__':
    n = int(input())
    
    result = calculate_last_digit_square_sum(n)
    print(result)
