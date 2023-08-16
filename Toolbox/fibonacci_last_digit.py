def fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    pisano_period = 60 
    
    fib = [0] * (pisano_period + 1)
    fib[1] = 1
    
    for i in range(2, pisano_period + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 10
    
    return fib[n % pisano_period]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
