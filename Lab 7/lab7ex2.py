def somme_de_trois(x):
    i=0
    while i<len(x)-2:
        if x[i]+x[i+1]+x[i+2]==0:
            return True
        i+=1
    return False

t = tuple(eval(input("Elements: ")))
print(somme_de_trois(t)) 