#Question 4 - Devoir 4

def read_raw(file):
    '''str->list of str
    Renvoie une liste de chaînes qui ont été stockées dans un fichier.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l):
    '''list of str->list of str
    La fonction prend en entrée une liste de caractères.
    Elle renvoie une nouvelle liste contenant les mêmes caractères que l
    sauf que un de chaque caractère apparaissant un nombre impair de fois
    dans l est supprimé et tous les caractères * sont supprimés 

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    l=[x for x in l if x!="*"]
    i=0
    while len(l)!=i:
        a=l.count(l[i])
        if (a%2)!=0:
            l.remove(l[i])
            if i!=0:   
                i-=1
        else:
            i+=1
    l.sort()
    
        
    clean_board=l
    return clean_board
    


def  is_rigorous(l):
    '''list of str->bool
    Renvoie True si chaque caractère de la liste apparaît exactement 2 fois ou si la liste est vide.
    Sinon, elle renvoie False. 
    
    Précondition: vous pouvez supposer que chaque élément de la liste apparaît un nombre pair de fois
    (c'est-à-dire que la liste est nettoyée par la fonction clean_up)
    >>>  is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>>  is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI

    a=[]
    for i in range(len(l)):
        a.append(l.count(l[i]))
    a.sort()
    if a[0] and a[-1]==2 or  a[0] and a[-1]==0:
        return True
    else:
        return False

    
#programme principal
b=['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E']
print("\nAvant clean-up:\n", b)
b=clean_up(b)
print("\nAprès clean-up:\n", b)
if is_rigorous(b):
    print("\nCette liste est maintenant rigoureuse; elle n’a aucun * et elle a "+str(len(b))+" caractères.")
else:
    print("\nCette liste n’a aucun * mais n'est pas rigoureuse et a "+str(len(b))+" caractères.")


"""Mon code marche mais je suis incapable d'ouvrir les fichier qu'on m'a donner avec le code qui était déjà là"""
     
