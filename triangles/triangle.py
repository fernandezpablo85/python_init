


def draw(n):
    w=[]
    triangle_steps=[]
    for stars in range(1,n+1):
        step=("*"*stars)
        for single_star in step:
            w.append(single_star)
        z=w
        w=[]
        t=" ".join(z)
        triangle_steps.append(t)
    return "\n".join(triangle_steps)
