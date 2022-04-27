def ajoute():
     for i in range(len(matrice)):
        for j in range(len(matrice[i])):
                matrice[i][j] = matrice[i][j]+1
    
            

def ajoute_V2(a):
    res = []
    for i in range(len(a)):
        row=[]
        for j in range(len(a[i])):
            row.append(a[i][j]+1)
        res.append(row)
    return res

# Programme Principale
m = int(input("Entrez le nombre de rangees: ")) 
n = int(input("Entrez le nombre de colonnes: ")) 
global matrice
matrice = []
i=0
while (i < m):
    j=0 
    matrice.append([]) 
    while j < n:
        v = int(input("matrice["+str(i)+","+str(j) +"]=")) 
        matrice[i].append(v)
        j=j+1
    i=i+1

print("\n")
print("La matrice est: ")
print(matrice)

print("Apres exécution de la fonction ajoute, la matrice est: ")
# Change la matrice originale
ajoute()
print(matrice)


print("Une nouvelle matrice créée avec ajoute_V2: ")
# Puisqu'on fait juste appellez la fonction sans l'assigné a une variable la matrice originale reste inchangé
print(ajoute_V2(matrice))

print("Apres exécution de la fonction ajoute_V2, la matrice initiale est: ")
print(matrice)