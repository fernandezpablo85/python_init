def add(a, b):
    return(a+b)

def is_even(n):
    return(n%2 == 0)
    
def is_odd(n):
    return(n%2 != 0)

def sum_all(*arr):
    add_all = 0
    if type(arr[0]) == list:
        arr=list(*arr)
    for numb in arr:
            add_all += numb
    return add_all

def is_prime(*p):
    pass