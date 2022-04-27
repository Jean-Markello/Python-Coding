def recherche_binaire(l,b):
    result=False
    l.sort()
    Npas=0
    i=0
    j=len(l)-1
    while i!= j+1:
        Npas+=1
        m=(i+j)//2
        if l[m]==b:
            result=True
            break
        elif l[m] < b:
            i=m+1
        elif l[m]>b:
            j=m-1
    print("le nombre de pas", Npas)
    return result
print(recherche_binaire([1, 2, 3, 4, 4, 5, 7, 9, 10, 13],10))