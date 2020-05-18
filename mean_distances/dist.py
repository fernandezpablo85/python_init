import math
import statistics

def mean_distance(p1, p2, p3):
    first_d = math.dist(p1,p2)
    second_d = math.dist(p2,p3)
    third_d = math.dist(p3,p1)
    return statistics.mean([first_d,second_d,third_d])
