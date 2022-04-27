def move_zeros_v1(x):
    tmp =[0]*len(x)
    i=0
    for xi in x:
        if xi !=0:
            tmp[i]=xi
            i+=1
    return tmp
l=[1,0,3,0,0,5,7]
print(l,move_zeros_v1(l))