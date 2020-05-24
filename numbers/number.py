import math

def add(a, b):
    return a + b


def is_even(n):
    try:
        if n%2 == 0 :
            return "Its Even"
    except ZeroDivisionError:
        return "cant apply to zero"


def is_odd(n):
    try:
        if n%2 !=0 :
            return "Its Odd"
    except ZeroDivisionError :
        return   "cant apply to zero"

def sum_all(arr):
    return sum(arr)

def is_prime(n):
    try:
        lista=[]
        for num in range(1,n+1):
            if n%num == 0:
                lista.append(num)
        if len(lista)<=2:
            return "Is_prime"
    except ZeroDivisionError :
        return   "cant apply to zero"


def most_popular(arr):
    """Return the number that appears more times in the array (the most popular one). If there are
    two numbers that appear the same number of times, return the lowest

    Examples:

    * [1] => 1
    * [1, 2] => 1
    * [1, 1, 3, 3, 3, 4, 4, 4] => 3"""

    dic={}
    max_list=[]

    for number in arr:
        if number not in dic:
            dic[number]=1
        elif number in dic:
            dic[number]=dic[number]+1

    result_key=math.inf

    for k,v in dic.items():
        if v == max(dic.values()) and k < result_key:
                result_key=k
                result_v=v
    return result_key
