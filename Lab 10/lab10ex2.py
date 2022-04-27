class CompteBancaire:
    def __init__(self,nom="Dupont",solde=1000):
        self.nom,self.solde=nom,solde

    def depot(self, somme):
        self.solde+=somme

    def retrait(self,somme):
        self.solde-=somme

    def affiche(self):
        print(f"Le solde du compte bancaire de {self.nom} est de {self.solde} dollars.")

class CompteEpargne(CompteBancaire):
    def __init__(self, nom="Dupont", solde=1000):
        super().__init__(nom=nom, solde=solde)
        self.taux=0.3

    def changeTaux(self,taux):
        self.taux=taux

    def capitalisation(self,nombreMois):
        print(f"Capitalisation sur {nombreMois} mois au taux mensuel de {self.taux} %")
        for m in range(nombreMois):
            self.solde*=(100+self.taux)/100
        
"""
compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()"""

c1 = CompteEpargne('Duvivier', 600)
c1.depot(350)
c1.affiche()
c1.capitalisation(12)
c1.affiche()
c1.changeTaux(.5)
c1.capitalisation(12)
c1.affiche()

