# Uses python3
m, n = map(int, input().split());

def fibonacci_sum(n):
    a = 0
    b = 1
    sum = 0
    for i in range(n):
        a,b = b%10, a+b%10
        sum = (sum + a) % 10
    return sum

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b % 10, a+b % 10
    return a

def fibonacci_partial(m,n):
    if m == n:
        return fibonacci(m)
    else:
        m_fib = fibonacci_sum(m-1)
        n_fib = fibonacci_sum(n)
        return (n_fib - m_fib) % 10

print(fibonacci_partial(m,n))
