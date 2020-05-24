def largest_repeat(numbers):
    """ Given an array of numbers, return the biggest value (x) that occurs exactly x times

    Examples:

    * [1, 2, 3, 4] => 1 (the only one that occurs the same number of times)
    * [1, 2, 2, 3, 3] => 2  (asdasdsad)
    * [1, 2, 3, 3, 3, 4, 4, 4, 4] => 4 (3 occurs 3 times and 4 occurs 4 times but 4 > 3)
    """
    dic={}
    repeat=[]

    for number in numbers:
        if number not in dic:
            dic[number]=1
        elif number in dic:
            dic[number]=dic[number]+1

    for k,v in dic.items():
        if k == v :
            repeat.append(k)
    return max(repeat)
