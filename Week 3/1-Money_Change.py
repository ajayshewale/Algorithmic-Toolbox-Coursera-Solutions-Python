# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = 0
    coins = coins + int(m/10)
    m = m % 10
    coins = coins + int(m/5)
    m = m % 5
    coins = m + coins

    return coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
