from random import shuffle

class Blackjack:
 valeurs={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
  
 def joue(self):
  '''jour un jeu'''   
  d = JeuDeCartes()
  d.battre()
  
  banque = Main('Banque')
  joueur = Main('Joueur')

  # donne deux cartes au joueur et deux cartes a la banque
  for i in range(2):  
    joueur.ajouteCarte(d.tireCarte())
    banque.ajouteCarte(d.tireCarte())

  # montre les mains
  banque.montreMain()
  joueur.montreMain()

  # tant que le joueur demande Carte!, la banque tire des cartes
  reponse = input('Carte? Oui ou non? (Par défaut oui) ')
  while reponse in ['','o','O','oui','Oui']:
    c = d.tireCarte()
    print("Vous avez:")
    print(c)
    joueur.ajouteCarte(c)
    if self.total(joueur) > 21:
       print("Vous avez dépassé 21. Vous avez perdu.")
       return   
    reponse = input('Carte? Oui ou non? (Par défaut oui) ')

  # la banque joue avec ses regles  
  while self.total(banque) < 17:
    print(banque)
    c = d.tireCarte()
    print("La banque a:")
    print(c)
    banque.ajouteCarte(c)
    if self.total(banque) > 21:
       print("La banque a dépassé 21. Vous avez gagné.")
       return

  # si 21 n'est pas depassée, compare les mains pour trouver le gagnat  
  self.compare(banque, joueur)

      
 def total(self, main):
    ''' (Main) -> int
    calcule la somme des valeur de toutes les cartes dans la main
    '''

    # a completer
    
    # calculez la somme de toutes les valeurs de la main
    somme, count_A=0,0
    print(main)
    for i in range(len(main)):
        if len(main[i])==2:
            try:
                int_value=int(main[i][0:1])
                somme+=int_value
            except ValueError:
                if main[i][0:1]=="A":
                    somme+=11
                    count_A+=1
                else:
                    somme+=10

        elif len(main)>2: #subject to change
            int_value=int(main[i][0:2])
            somme+=int_value
    
    # while la somme > 21 et il y a des As, deduisez 10 points pour chaque As
    while somme > 21 and count_A>0:
        somme-=10

    return somme 

 def compare(self, banque, joueur):
    ''' (Main, Main) -> None
    Compare la main du joueur avec la main de la banque
    et affiche de messages
    '''

    # a completer

    # applelez la methode self.total pour la banque et pour le joueur
    total_bank= self.total(banque)
    total_joueur=self.total(joueur)

    # si le total de la banque > le total du joueur affichez 'Vous avez perdu.'
    if total_joueur<total_bank:
        print('Vous avez perdu.')

    # si le total de la banque < le total du joueur affichez 'Vous avez gagné.'   
    elif total_joueur>total_bank:
        print('Vous avez gagné.')

    # en cas d'egalite, si le total est 21m si la banque a un blackjack
    # affichez 'Vous avez perdu.'; si le joueur a un blackjack 'Vous avez gagné.' 
    elif total_bank==21 and total_joueur==21:
        for x,v in zip(banque,joueur):
            if x[0:2]==10 and x[0:1]=="A":
                print('Vous avez perdu.')
            if v[0:2]==10 and v[0:1]=="A":
                print('Vous avez gagné.')

    # sinon, affichez 'Egalité.'
            else:
                print('Vous avez gagné.')
    else:
        print('Egalité.')

       
class Main(object):
    '''represente une main des cartes a jouer'''

    def __init__(self, joueur):
        '''(Main, str)-> none
        initialise le nom du joueur et la liste de cartes avec liste vide'''

        # a completer
        self.joueur=joueur
        self.main=[]
        print(type(self.main))

    def ajouteCarte(self, carte):
        '''(Main, Carte) -> None
        ajoute une carte a la main'''
        
        # a completer
        self.main.append(carte)

    def montreMain(self):
        '''(Main)-> None
        affiche le nom du joueur et la main'''

        # a completer
        print(f"{self.joueur}: {self.main}")
                
    def __eq__(self, autre):
        '''retourne True si les main ont les meme cartes
           dans la meme ordre'''
        
        # a completer
        return self.main==autre.main


    def __repr__(self):
        '''retourne une representation de l'objet'''
        
        # a completer
        return 'Main('+self.joueur+', '+ str(self.main)+')'

class Carte:
    '''represente une carte a jouer'''

    def __init__(self, valeur, couleur):
        '''(Carte,str,str)->None        
        initialise la valeur et la couleur de la carte'''
        self.valeur = valeur
        self.couleur = couleur  # pique, coeur, trefle ou carreau

    def __repr__(self):
        '''(Carte)->str
        retourne une representation de l'objet'''
        return 'Carte('+self.valeur+', '+self.couleur+')'

    def __eq__(self, autre):
        '''(Carte,Carte)->bool
        self == autre si la valeur et la couleur sont les memes'''
        return self.valeur == autre.valeur and self.couleur == autre.couleur

class JeuDeCartes:
    '''represente une jeu de 52 cartes'''
    # valeurs et couleurs sont des variables de classe
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    # couleurs est un set de 4 symboles Unicode qui representent les 4 couleurs
    # pique, coeur, trefle ou carreau
    
    def __init__(self):
        'initialise le paquet de 52 cartes'
        self.paquet = []          # paquet vide au debut
        for couleur in JeuDeCartes.couleurs: 
            for valeur in JeuDeCartes.valeurs: # variables de classe
                # ajoute une Carte de valeur et couleur
                self.paquet.append(Carte(valeur,couleur))

    def tireCarte(self):
        '''(JeuDeCartes)->Carte
        distribue une carte, la premiere du paquet'''
        return self.paquet.pop()

    def battre(self):
        '''(JeuDeCartes)->None
        pour battre le jeu des cartes'''
        shuffle(self.paquet)

    def __repr__(self):
        '''retourne une representation de l'objet'''
        return 'Paquet('+str(self.paquet)+')'

    def __eq__(self, autre):
        '''retourne True si les paquets ont les meme cartes
           dans la meme ordre'''
        return self.paquet == autre.paquet
    
    
b = Blackjack()
b.joue()

