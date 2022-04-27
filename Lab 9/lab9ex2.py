def bubbleSort(l):
    echange= True 
    Npas= 0
    j=len(l)-1
    while echange:
        echange=False
        for i in range(j):
            Npas +=1
            if l[i]>l[i+1]:
                echange=True
                l[i], l[i+1]= l[i+1], l[i]
        j-=1
    print("nombre de pas", Npas)
l=[1,92,94,1,59,2,65,64,45,79]
bubbleSort(l)
print(l)
