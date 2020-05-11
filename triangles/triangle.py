def draw(n):
    triangulo = []
    for i in range (0,n):
        triangulo.append(line(i+1))
    return '\n'.join(triangulo)

def line(x):
    new_line = []
    for i in range(0,x):
        new_line.append('*')
    return ' '.join(new_line)    