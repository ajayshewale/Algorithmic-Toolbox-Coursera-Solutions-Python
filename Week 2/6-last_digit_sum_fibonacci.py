# Uses python3
fib_number = int(input())

def fibonacci(n):
    a = 0
    b = 1
    sum = 0
    for i in range(n):
        a,b = b%10, a+b%10
        sum = (sum + a) % 10
    return sum

print(fibonacci(fib_number))
