def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
    # a completer

   for i in range(len(tab)):
      for c in range(len(tab[0])):
         if tab[i][c]!="-":
            tab[i][c]="-"
    # retourne rien

      
def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    # a completer
    L=testLignes(tab)
    C=testCols(tab)
    D=testDiags(tab)
    M=testMatchNul(tab)
    if L=="O" or C=="O" or D=="O" :
       print("Joueur O a gagné!")
       return True
    elif L=="X" or C=="X" or D=="X":
       print("Joueur X a gagné!")
       return True
    elif M==True:
       print("Match nul")
       return True
    elif M==False:
       return False  # a changer

 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer

   for i in range(len(tab)):
      count=0
      count2=0
      for c in range(len(tab[0])):
         if tab[i][c]=="O":
            count+=1
            if count==3:
               return "O"
         if tab[i][c]=="X":
            count2+=1
            if count2==3:
               return "X"
   return '-' # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant 

  
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   for c in range(len(tab)):
      count=0
      count2=0
      for i in range(len(tab[0])):
         if tab[i][c]=="O":
            count+=1
            if count==3:
               return "O"
         if tab[i][c]=="X":
            count2+=1
            if count2==3:
               return "X"
            
  
   return '-'   #a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   count,count2=0,0
   for  i, x in zip(range(len(tab)),range(len(tab))):
      if tab[i][x]=="O":
         count+=1
         if count==3:
            return "O"
      if tab[i][x]=="X":
         count2+=1
         if count2==3:
            return "X"
            

   count,count2=0,0
   for c,v in zip(range(len(tab)-1,-1,-1), range(len(tab))):
         if tab[c][v]=="X":
            count2+=1
            if count2==3:
               return "X"
         if tab[c][v]=="O":
            count+=1
            if count==3:
               return "O"

    
   return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   for i in range(len(tab)):
      for x in tab[i]:
         if x=="-":
            return False
   
   return True  # a changer

