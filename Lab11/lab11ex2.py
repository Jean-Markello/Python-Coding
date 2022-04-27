def iniListe(l,n):
    if n!=0:
        l.insert(0,n-1)
        iniListe(l,n-1)

l=[]
n=int(input("SVP donner un n: "))
iniListe(l,n)
print(l)
