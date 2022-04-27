def affichematrice(matrice):
    for i in matrice: # visite chaque ligne
        for j in i: # visite chaque element de la ligne
            print(j, end=" ")
        print()

def inputmatrice():
    print("Entrez les nombres avec des espaces entre les colonnes.")
    print("Une rangee par ligne, et une ligne vide a la fin.")

    matrice=[]
    while True:
        ligne=input()
        if not ligne: break
        valeurs=ligne.split()
        rangee = [int(val) for val in valeurs]
        matrice.append(rangee)
    return matrice

def transpose(a):
    at=[]
    c=0
    while c<len(a[0]):
        L=0
        at.append([])
        while L <len(a):
            at[c].append(a[L][c])
            L+=1
        c=c+1
    return at

b=inputmatrice()
B=transpose(b)
affichematrice(B)