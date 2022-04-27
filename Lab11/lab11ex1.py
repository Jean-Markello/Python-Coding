def vérifChiffres(a,n):
    if n==0:
        v=True
    else:
        if 0<=a[n-1]<=9:
            v=vérifChiffres(a,n-1)
        else:
            v=False

    return v

a=[1,1,2,3,4,2,3,9]
print(vérifChiffres(a,len(a)))
