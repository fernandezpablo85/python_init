def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0
    
def is_odd(n):
    return n % 2 != 0

def sum_all(*arr):
    if len(arr) == 0:
        return 0

    nums = arr[0] if isinstance(arr[0], list) else arr
    return sum(nums)

def is_prime(*p):
    pass