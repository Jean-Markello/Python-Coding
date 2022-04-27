def hey(m):
    s=0.0
    k=0
    while k<=m:
        s+=(1/2)**k
        k+=1
    return s
    

print(hey(3))
