class Voiture:
    def __init__(self, marque = 'Ford', couleur = 'rouge'):
        self.marque=marque
        self.couleur=couleur
        self.pilote='personne'
        self.vitesse=0
    
    def choix_conducteur(self, nom):
        self.pilote=nom
    
    def accelerer(self, taux, duree):
        if self.pilote=="personne":
            print("Cette voiture n'a pas de conducteur !")
        else:
            self.vitesse+=taux*duree
    
    def affiche_tout(self):
        print(f"{self.marque} {self.couleur} pilotée par {self.pilote}, vitesse= {self.vitesse} m/s")

    def __repr__(self) -> str:
        return f"{self.marque} {self.couleur} pilotée par {self.pilote}, vitesse= {self.vitesse} m/s"

    def __eq__(self, autre):
        return self.marque==autre.marque and \
            self.couleur==autre.couleur and \
            self.pilote==autre.pilote and \
            self.vitesse==autre.vitesse

a1 = Voiture('Peugeot', 'bleue')
a2 = Voiture(couleur = 'verte')
a3 = Voiture('Mercedes')
a1.choix_conducteur('Roméo')
a2.choix_conducteur('Juliette')
a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11)
print(a3, "djdjdjfjd")
a2.affiche_tout()
a3.affiche_tout()
print(a1==a2)
print(Voiture()==Voiture())
print(a1)
