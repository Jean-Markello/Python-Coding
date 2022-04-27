joueur=["A","10"]
banque=["10", "A"]
total_bank=21
total_joueur=21


if total_bank==21 and total_joueur==21:
    if banque[0][0:2]=="10" and banque[1][0:1]=="A" or banque[1][0:1]=="A" and banque[0][0:2]=="10" and joueur[0][0:2]=="10" and joueur[1][0:1]=="A" or joueur[0][0:1]=="A" and joueur[1][0:2]=="10":
        print("egalite")
    elif banque[0][0:2]=="10" and banque[1][0:1]=="A" or banque[1][0:1]=="A" and banque[0][0:2]=="10":
        print('Vous avez perdu.')
        print("hey")
    elif joueur[0][0:2]=="10" and joueur[1][0:1]=="A" or joueur[0][0:1]=="A" and joueur[1][0:2]=="10":
        print('Vous avez gagné.')
        print("hey")
    else:
        print("egale")
print(joueur[0][0:2])
print("hey")