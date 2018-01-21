# Uses python3

def pisano(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range (1, m*m):
            c = (a+b) % m
            a = b
            b = c
            if (a==0 and b==1):
                return i


def huge_fib(n, m):
    remainder = n % pisano(m)
    first = 0
    second = 1
    res = remainder
    for i in range(1, remainder):
        res = (first+second) % m
        first = second
        second = res

    return res % m

n,m = map(int, input().split());
print(huge_fib(n,m))
