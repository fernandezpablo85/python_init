def add(a, b):
    return(a+b)

def is_even(n):
    return(n%2 == 0)
    
def is_odd(n):
    return(n%2 != 0)

def sum_all(*arr):
    add_all = 0
    for numb in arr:
        add_all = add_all + numb
    return add_all