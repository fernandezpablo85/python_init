import math

"""
print(mean_distance(  (0, 0), (2, 0), (2, 2)))
ejecuto la funcion y el resultado es este : 2.2761423749153966/
me tira error,  por lo que veo la comprobacion la hace con raiz de 8 que es :
2.82842712475

"""

def mean_distance(p1, p2, p3):
    """ Given 3 points or (x, y) pairs, obtain the mean distance between them"""

    p1_p2= math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    p1_p3=math.sqrt((p3[0]-p1[0])**2 + (p3[1]-p1[1])**2)
    p2_p3=math.sqrt((p3[0]-p2[0])**2 + (p3[1]-p2[1])**2)
    list_points=[p1_p2,p1_p3,p2_p3]

    return  sum(list_points)/len(list_points)
