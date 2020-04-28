def draw(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('*',end=' ')
        print ('\n')


def drawn(n):
    for i in range(0,n):
        print((i+1)*'* ')
