def add(a, b):
    print(a+b)

def is_even(n):
    print(n%2 == 0)
    
def is_odd(n):
    print(n%2 != 0)

def sum_all(arr):
    add_all = 0
    for numb in arr:
        add_all = (add_all + numb)
    print(add_all)