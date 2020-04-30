def draw(n,t=1):
    while n > 0:
        print('* '*(n-n+t))
        return draw(n-1,t+1)

def draws(i):
    #if i == 0:
    #    return ""
    #else:
    while i > 0:
        print('* '*i)
        return draws(i-1)
    
def triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print(' ' * ( t + 1 ) + '*' * ( i * 2 - 1 ))
        return triangle( i - 1, t + 1 )
