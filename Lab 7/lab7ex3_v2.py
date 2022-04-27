def move_zeros_v2(x):
    tmp =[0]*len(x)
    print(tmp)
    i=0
    for xi in x:
        if xi !=0:
            tmp[i]=xi
            i+=1
    for i in range(len(x)):
        x[i]=tmp[i]
l=[1,0,3,0,0,5,7]
z=move_zeros_v2(l)
print(l,z)