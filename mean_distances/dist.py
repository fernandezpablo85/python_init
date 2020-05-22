import math

def mean_distance(p1, p2, p3):
    """ Given 3 points or (x, y) pairs, obtain the mean distance between them"""
    pass
    p1_p2= math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    p1_p3=math.sqrt((p3[0]-p1[0])**2 + (p3[1]-p1[1])**2)
    p2_p3=math.sqrt((p3[0]-p2[0])**2 + (p3[1]-p2[1])**2)
    list_points=[p1_p2,p1_p3,p2_p3]

    return  sum(list_points)/len(list_points)

p1, p2, p3 = (-3, -9), (2, 0), (2, 2)

print (mean_distance(p1, p2, p3))
