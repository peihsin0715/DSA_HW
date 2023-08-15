def get_pisano_period(m):
    a = 0
    b = 1
    pisano_period = [a, b]
    
    while True:
        a, b = b, (a + b) % m
        pisano_period.append(b)
        if a == 0 and b == 1:
            break
    
    return pisano_period[:-2]  # Remove the last two elements, which belong to the next cycle

def fibonacci_huge(n, m):
    if n <= 1:
        return n
    
    pisano_period = get_pisano_period(m)
    period_length = len(pisano_period)
    remainder = n % period_length
    
    return pisano_period[remainder]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
