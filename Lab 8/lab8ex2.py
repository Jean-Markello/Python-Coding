def somme_matrices(a,b):
    i=0
    c=[]
    while i<len(a):
        j=0
        tmp=[]
        c.append(tmp)
        while j<len(a[0]):
            c[i].append(a[i][j]+b[i][j])
            j+=1
        i+=1
    return c

a=[[1,2],[3,4]]
b= [[1,1],[1,1]]
print("c", somme_matrices(a,b))