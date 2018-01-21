# Uses python3
fib_number = int(input())

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b % 10, a+b % 10
    return a

print(fibonacci(fib_number))
