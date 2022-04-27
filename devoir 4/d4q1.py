#Cette fonction retourne le # de séquence Maximale de charactère qui se suit
def séquenceMax(liste):
    a=[]
    for i in range(len(liste)):
        a.append(liste.count(liste[i]))
    a=max(a)
    return a

#Prend l'entrer de l'usage
inp= input("Veuillez entrer une liste de valeurs séparées par des virgules: ").split(",")
inp= [int(b) for b in inp]
print(séquenceMax(inp))
