#Question 5 - Devoir 4
# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''

     
     donneur=[]
     autre=[]


     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     pre=len(p)//2
     donneur= p[:pre]
     autre= p[pre:]
     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
     
    b=[]
    a=[]
    n=[]
    print(l)

    for x in l:
        if len(x)==3:
            b.append(x[0:2])
        else:
            b.append(x[0:1])
    
    
    print(len(b))
    for j in range(len(l)):
        print(b.count(b[j]))
        a.append(b.count(b[j]))
   
    
    
    for k in range(len(a)):
        if a[k]%2==0:                         #changement de a[k]>1
            n.append(k)
    
    for index in sorted(n, reverse=True):
        del l[index]

   
    
    random.shuffle(l)
    
   

    return l


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    for x in range(len(p)):
        print(p[x]," ")
    


    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     
     print("J'ai", n+1, "cartes. Si 0 est la position de ma premiere carte et", n, "est la position de ma derniere carte, laquelle de mes cartes voulez-vous?")
     choix = int(input("SVP entrez un entier de 0 a " + str(n) + " : "))   #modifier affichage + le +1

     if choix > n:
         entrez_position_valide(n)
     else:
         print("Vous avez choisi la carte", choix)
         return choix

#cette fonction vérifie s'il y a un gagnnt
def verifier_gagnant(humain, donneur):
    if len(humain)==0:
        print("J'ai terminé toutes les cartes.\nFélicitations! Vous, Humain, vous avez gagné.")
        return True
    elif len(donneur)==0:
        print("J'ai terminé toutes les cartes.\nVous avez perdu! Moi, Robot, j'ai gagné.")
        return True
        

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p) 
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
    
     affiche_cartes(humain)
     affiche_cartes(donneur)
     

     while True: #on pourrait juste mettre while True
        print(donneur)
        print("Votre tour\nVotre main est", humain)
        #Tour de l'humain:
        option=entrez_position_valide(len(donneur)-1)   # mis un -1 pour modifier pour l'affichage du message dans la fonction
        print("Vous avez demandé ma", option,"ère/ème carte.")
        
        print("La voilà, c'est un", donneur[option])
        humain.append(donneur[option])
        donneur.remove(donneur[option])
        humain=elimine_paires(humain)
        print(donneur)
        print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:\n",humain)
        attend_le_joueur()

        verification=verifier_gagnant(humain, donneur)
        if verification==True:
            break

        #Tour de l'ordi:
        ordi=random.randint(0,(len(humain)-1))
        print("Mon tour\nJ'ai pris votre", ordi, "ème/ère carte")
        print(ordi)

        #inverser leur position
        donneur.append(humain[ordi])   
        humain.remove(humain[ordi])    
        
        
        
        donneur=elimine_paires(donneur)

        verification=verifier_gagnant(humain, donneur)
        if verification==True:
            break

        attend_le_joueur()

	 
# programme principale
joue()

