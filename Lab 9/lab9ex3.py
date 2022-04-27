def tri_par_insertion(l):
    Npas=0
    i =1
    while i< len(l):
        Npas +=1
        temp=l[i]
        j=i-1
        while j>=0 and temp<l[j]:
            Npas+=1
            l[j+1]= l[j]
            j-=1
        l[j+1]=temp
        i+=1
    print("le nombre de pas", Npas)

l=[3, 4, -1, 7, 2, 5, 16, -2, 17, 7, 82, -1]
tri_par_insertion(l)
print(l)