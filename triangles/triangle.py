def draw(n):
    triangulo = []
    for i in range (0,n):
        triangulo.append(line(i+1))
    return '\n'.join(triangulo)

def line(x):
    return ' '.join(['*'] * x)