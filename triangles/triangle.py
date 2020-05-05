def draw(n):
    triangulo = []
    for i in range (0,n):
        triangulo.append(line(i+1))
    print('\n'.join(triangulo))
    #return '\n'.join(triangulo)

def line(x):
    linea = []
    for i in range(0,x):
        linea.append('*')
    return ' '.join(linea)    
