def histo_n(x):
    dic={}
    for c in x:
        dic[c]=dic.get(c,0)+1
    print(dic)
    return dic

t = tuple(eval(input("Elements: ")))
b=(histo_n(t))
b=list(b.items())
b.sort()
print(b)