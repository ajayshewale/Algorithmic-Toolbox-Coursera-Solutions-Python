# Uses python3
n = int(input())
a = [int(x) for x in input().split()]

def MaxPairwiseProductFast(arr):
#   assert(len(a) == n)
    arr = sorted(arr)
    assert(len(arr) == n)
    print(arr[n-1]*arr[n-2])

MaxPairwiseProductFast(a)
