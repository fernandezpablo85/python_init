def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n%2 != 0


def is_prime(n):
    
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    for i in range(3,n):
        if n % i == 0:
            return False
    return True
        

def sum_all(arr):
    return sum(arr)


def most_popular(arr):

    counter = 0
    num = arr[0]

    for i in arr:
        frecuency = arr.count(i)
        if (frecuency > counter):
            counter = frecuency
            num = i
    
    return num
