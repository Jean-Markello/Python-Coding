import math
import sys

def nombre_divisble(a, list_1):
    print(len([i for i in list_1 if i%a == 0]))


def main():
    n = int(input("SVP, Entrez un entier : "))

    # Saisit la liste
    Num_List=[]
    Num_List = input("Veuillez entrer une liste de valeurs séparées par des virgules: ").split(',')

    # Convertit liste en int
    for i in range(0, len(Num_List)):
        Num_List[i] = int(Num_List[i])

    nombre_divisble(n, Num_List)

if __name__ == "__main__":
    main()
