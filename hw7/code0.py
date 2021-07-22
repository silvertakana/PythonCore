def list_total(l):
    y =0
    for x in l:
        y+=x
    return y
    
def list_mult(l):
    y = 1
    for x in l:
        y*=x
    return y
print(list_mult([3,7]))
