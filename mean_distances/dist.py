import math

def mean_distance(p1, p2, p3):
    return math.dist(p1,p3)

def mean_distance_t(p1, p2, p3):
    first_d = math.dist(p1,p2)
    second_d = math.dist(p2,p3)
    third_d = math.dist(p3,p1)
    print( first_d,second_d,third_d)
    return (first_d+second_d+third_d)/3


    #""" Given 3 points or (x, y) pairs, obtain the mean distance between them"""
    #pass
